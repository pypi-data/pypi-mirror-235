from __future__ import annotations

import enum
import logging
import os
import uuid
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Type,
)

from promptmanager.script.base.docstore.document import Document
from promptmanager.script.base.schema.embeddings import Embeddings
from promptmanager.script.base.schema.vectorstore import VectorStore
from promptmanager.script.base.utils import get_from_env
from promptmanager.script.base.vectorstores.utils import DistanceStrategy

DEFAULT_DISTANCE_STRATEGY = DistanceStrategy.COSINE
DISTANCE_MAPPING = {
    DistanceStrategy.EUCLIDEAN_DISTANCE: "euclidean",
    DistanceStrategy.COSINE: "cosine",
}


class SearchType(str, enum.Enum):
    """Enumerator of the Distance strategies."""

    VECTOR = "vector"
    HYBRID = "hybrid"


DEFAULT_SEARCH_TYPE = SearchType.VECTOR


def _get_search_index_query(search_type: SearchType) -> str:
    type_to_query_map = {
        SearchType.VECTOR: (
            "CALL db.index.vector.queryNodes($index, $k, $embedding) YIELD node, score "
        ),
        SearchType.HYBRID: (
            "CALL { "
            "CALL db.index.vector.queryNodes($index, $k, $embedding) "
            "YIELD node, score "
            "RETURN node, score UNION "
            "CALL db.index.fulltext.queryNodes($keyword_index, $query, {limit: $k}) "
            "YIELD node, score "
            "WITH collect({node:node, score:score}) AS nodes, max(score) AS max "
            "UNWIND nodes AS n "
            "RETURN n.node AS node, (n.score / max) AS score "  # We use 0 as min
            "} "
            "WITH node, max(score) AS score ORDER BY score DESC LIMIT $k "  # dedup
        ),
    }
    return type_to_query_map[search_type]


def check_if_not_null(props: List[str], values: List[Any]) -> None:
    for prop, value in zip(props, values):
        if not value:
            raise ValueError(f"Parameter `{prop}` must not be None or empty string")


def sort_by_index_name(
    lst: List[Dict[str, Any]], index_name: str
) -> List[Dict[str, Any]]:
    """Sort first element to match the index_name if exists"""
    return sorted(lst, key=lambda x: x.get("index_name") != index_name)


class Neo4jVector(VectorStore):
    """`Neo4j` vector index.

    To use, you should have the ``neo4j`` python package installed.

    Args:
        url: Neo4j connection url
        username: Neo4j username.
        password: Neo4j password
        database: Optionally provide Neo4j database
                  Defaults to "neo4j"
        embedding: Any embedding function implementing
            `promptmanager.embeddings.base.Embeddings` interface.
        distance_strategy: The distance strategy to use. (default: COSINE)
        pre_delete_collection: If True, will delete existing data if it exists.
            (default: False). Useful for testing.

    Example:
        .. code-block:: python

            from promptmanager.script.base.vectorstores.neo4j_vector import Neo4jVector
            from promptmanager.script.base.embeddings.openai import OpenAIEmbeddings

            url="bolt://localhost:7687"
            username="neo4j"
            password="pleaseletmein"
            embeddings = OpenAIEmbeddings()
            vectorestore = Neo4jVector.from_documents(
                embedding=embeddings,
                documents=docs,
                url=url
                username=username,
                password=password,
            )


    """

    def __init__(
        self,
        embedding: Embeddings,
        *,
        search_type: SearchType = SearchType.VECTOR,
        username: Optional[str] = None,
        password: Optional[str] = None,
        url: Optional[str] = None,
        keyword_index_name: Optional[str] = "keyword",
        database: str = "neo4j",
        index_name: str = "vector",
        node_label: str = "Chunk",
        embedding_node_property: str = "embedding",
        text_node_property: str = "text",
        distance_strategy: DistanceStrategy = DEFAULT_DISTANCE_STRATEGY,
        logger: Optional[logging.Logger] = None,
        pre_delete_collection: bool = False,
        retrieval_query: str = "",
        relevance_score_fn: Optional[Callable[[float], float]] = None,
    ) -> None:
        try:
            import neo4j
        except ImportError:
            raise ImportError(
                "Could not import neo4j python package. "
                "Please install it with `pip install neo4j`."
            )

        # Allow only cosine and euclidean distance strategies
        if distance_strategy not in [
            DistanceStrategy.EUCLIDEAN_DISTANCE,
            DistanceStrategy.COSINE,
        ]:
            raise ValueError(
                "distance_strategy must be either 'EUCLIDEAN_DISTANCE' or 'COSINE'"
            )

        # Handle if the credentials are environment variables

        # Support URL for backwards compatibility
        url = os.environ.get("NEO4J_URL", url)
        url = get_from_env("url", "NEO4J_URI", url)
        username = get_from_env("username", "NEO4J_USERNAME", username)
        password = get_from_env("password", "NEO4J_PASSWORD", password)
        database = get_from_env("database", "NEO4J_DATABASE", database)

        self._driver = neo4j.GraphDatabase.driver(url, auth=(username, password))
        self._database = database
        self.schema = ""
        # Verify connection
        try:
            self._driver.verify_connectivity()
        except neo4j.exceptions.ServiceUnavailable:
            raise ValueError(
                "Could not connect to Neo4j database. "
                "Please ensure that the url is correct"
            )
        except neo4j.exceptions.AuthError:
            raise ValueError(
                "Could not connect to Neo4j database. "
                "Please ensure that the username and password are correct"
            )

        # Verify if the version support vector index
        self.verify_version()

        # Verify that required values are not null
        check_if_not_null(
            [
                "index_name",
                "node_label",
                "embedding_node_property",
                "text_node_property",
            ],
            [index_name, node_label, embedding_node_property, text_node_property],
        )

        self.embedding = embedding
        self._distance_strategy = distance_strategy
        self.index_name = index_name
        self.keyword_index_name = keyword_index_name
        self.node_label = node_label
        self.embedding_node_property = embedding_node_property
        self.text_node_property = text_node_property
        self.logger = logger or logging.getLogger(__name__)
        self.override_relevance_score_fn = relevance_score_fn
        self.retrieval_query = retrieval_query
        self.search_type = search_type
        # Calculate embedding dimension
        self.embedding_dimension = len(embedding.embed_query("foo"))

        # Delete existing data if flagged
        if pre_delete_collection:
            from neo4j.exceptions import DatabaseError

            self.query(
                f"MATCH (n:`{self.node_label}`) "
                "CALL { WITH n DETACH DELETE n } "
                "IN TRANSACTIONS OF 10000 ROWS;"
            )
            # Delete index
            try:
                self.query(f"DROP INDEX {self.index_name}")
            except DatabaseError:  # Index didn't exist yet
                pass

    def query(
        self, query: str, *, params: Optional[dict] = None
    ) -> List[Dict[str, Any]]:
        """
        This method sends a Cypher query to the connected Neo4j database
        and returns the results as a list of dictionaries.

        Args:
            query (str): The Cypher query to execute.
            params (dict, optional): Dictionary of query parameters. Defaults to {}.

        Returns:
            List[Dict[str, Any]]: List of dictionaries containing the query results.
        """
        from neo4j.exceptions import CypherSyntaxError

        params = params or {}
        with self._driver.session(database=self._database) as session:
            try:
                data = session.run(query, params)
                return [r.data() for r in data]
            except CypherSyntaxError as e:
                raise ValueError(f"Cypher Statement is not valid\n{e}")

    def verify_version(self) -> None:
        """
        Check if the connected Neo4j database version supports vector indexing.

        Queries the Neo4j database to retrieve its version and compares it
        against a target version (5.11.0) that is known to support vector
        indexing. Raises a ValueError if the connected Neo4j version is
        not supported.
        """
        version = self.query("CALL dbms.components()")[0]["versions"][0]
        if "aura" in version:
            version_tuple = tuple(map(int, version.split("-")[0].split("."))) + (0,)
        else:
            version_tuple = tuple(map(int, version.split(".")))

        target_version = (5, 11, 0)

        if version_tuple < target_version:
            raise ValueError(
                "Version index is only supported in Neo4j version 5.11 or greater"
            )

    def retrieve_existing_index(self) -> Optional[int]:
        """
        Check if the vector index exists in the Neo4j database
        and returns its embedding dimension.

        This method queries the Neo4j database for existing indexes
        and attempts to retrieve the dimension of the vector index
        with the specified name. If the index exists, its dimension is returned.
        If the index doesn't exist, `None` is returned.

        Returns:
            int or None: The embedding dimension of the existing index if found.
        """

        index_information = self.query(
            "SHOW INDEXES YIELD name, type, labelsOrTypes, properties, options "
            "WHERE type = 'VECTOR' AND (name = $index_name "
            "OR (labelsOrTypes[0] = $node_label AND "
            "properties[0] = $embedding_node_property)) "
            "RETURN name, labelsOrTypes, properties, options ",
            params={
                "index_name": self.index_name,
                "node_label": self.node_label,
                "embedding_node_property": self.embedding_node_property,
            },
        )
        # sort by index_name
        index_information = sort_by_index_name(index_information, self.index_name)
        try:
            self.index_name = index_information[0]["name"]
            self.node_label = index_information[0]["labelsOrTypes"][0]
            self.embedding_node_property = index_information[0]["properties"][0]
            embedding_dimension = index_information[0]["options"]["indexConfig"][
                "vector.dimensions"
            ]

            return embedding_dimension
        except IndexError:
            return None

    def retrieve_existing_fts_index(
        self, text_node_properties: List[str] = []
    ) -> Optional[str]:
        """
        Check if the fulltext index exists in the Neo4j database

        This method queries the Neo4j database for existing fts indexes
        with the specified name.

        Returns:
            (Tuple): keyword index information
        """

        index_information = self.query(
            "SHOW INDEXES YIELD name, type, labelsOrTypes, properties, options "
            "WHERE type = 'FULLTEXT' AND (name = $keyword_index_name "
            "OR (labelsOrTypes = [$node_label] AND "
            "properties = $text_node_property)) "
            "RETURN name, labelsOrTypes, properties, options ",
            params={
                "keyword_index_name": self.keyword_index_name,
                "node_label": self.node_label,
                "text_node_property": text_node_properties or [self.text_node_property],
            },
        )
        # sort by index_name
        index_information = sort_by_index_name(index_information, self.index_name)
        try:
            self.keyword_index_name = index_information[0]["name"]
            self.text_node_property = index_information[0]["properties"][0]
            node_label = index_information[0]["labelsOrTypes"][0]
            return node_label
        except IndexError:
            return None

    def create_new_index(self) -> None:
        """
        This method constructs a Cypher query and executes it
        to create a new vector index in Neo4j.
        """
        index_query = (
            "CALL db.index.vector.createNodeIndex("
            "$index_name,"
            "$node_label,"
            "$embedding_node_property,"
            "toInteger($embedding_dimension),"
            "$similarity_metric )"
        )

        parameters = {
            "index_name": self.index_name,
            "node_label": self.node_label,
            "embedding_node_property": self.embedding_node_property,
            "embedding_dimension": self.embedding_dimension,
            "similarity_metric": DISTANCE_MAPPING[self._distance_strategy],
        }
        self.query(index_query, params=parameters)

    def create_new_keyword_index(self, text_node_properties: List[str] = []) -> None:
        """
        This method constructs a Cypher query and executes it
        to create a new full text index in Neo4j.
        """
        node_props = text_node_properties or [self.text_node_property]
        fts_index_query = (
            f"CREATE FULLTEXT INDEX {self.keyword_index_name} "
            f"FOR (n:`{self.node_label}`) ON EACH "
            f"[{', '.join(['n.`' + el + '`' for el in node_props])}]"
        )
        self.query(fts_index_query)

    @property
    def embeddings(self) -> Embeddings:
        return self.embedding

    @classmethod
    def __from(
        cls,
        texts: List[str],
        embeddings: List[List[float]],
        embedding: Embeddings,
        metadatas: Optional[List[dict]] = None,
        ids: Optional[List[str]] = None,
        create_id_index: bool = True,
        search_type: SearchType = SearchType.VECTOR,
        **kwargs: Any,
    ) -> Neo4jVector:
        if ids is None:
            ids = [str(uuid.uuid1()) for _ in texts]

        if not metadatas:
            metadatas = [{} for _ in texts]

        store = cls(
            embedding=embedding,
            search_type=search_type,
            **kwargs,
        )
        # Check if the vector index already exists
        embedding_dimension = store.retrieve_existing_index()

        # If the vector index doesn't exist yet
        if not embedding_dimension:
            store.create_new_index()
        # If the index already exists, check if embedding dimensions match
        elif not store.embedding_dimension == embedding_dimension:
            raise ValueError(
                f"Index with name {store.index_name} already exists."
                "The provided embedding function and vector index "
                "dimensions do not match.\n"
                f"Embedding function dimension: {store.embedding_dimension}\n"
                f"Vector index dimension: {embedding_dimension}"
            )

        if search_type == SearchType.HYBRID:
            fts_node_label = store.retrieve_existing_fts_index()
            # If the FTS index doesn't exist yet
            if not fts_node_label:
                store.create_new_keyword_index()
            else:  # Validate that FTS and Vector index use the same information
                if not fts_node_label == store.node_label:
                    raise ValueError(
                        "Vector and keyword index don't index the same node label"
                    )

        # Create unique constraint for faster import
        if create_id_index:
            store.query(
                "CREATE CONSTRAINT IF NOT EXISTS "
                f"FOR (n:`{store.node_label}`) REQUIRE n.id IS UNIQUE;"
            )

        store.add_embeddings(
            texts=texts, embeddings=embeddings, metadatas=metadatas, ids=ids, **kwargs
        )

        return store

    def add_embeddings(
        self,
        texts: Iterable[str],
        embeddings: List[List[float]],
        metadatas: Optional[List[dict]] = None,
        ids: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> List[str]:
        """Add embeddings to the vectorstore.

        Args:
            texts: Iterable of strings to add to the vectorstore.
            embeddings: List of list of embedding vectors.
            metadatas: List of metadatas associated with the texts.
            kwargs: vectorstore specific parameters
        """
        if ids is None:
            ids = [str(uuid.uuid1()) for _ in texts]

        if not metadatas:
            metadatas = [{} for _ in texts]

        import_query = (
            "UNWIND $data AS row "
            "CALL { WITH row "
            f"MERGE (c:`{self.node_label}` {{id: row.id}}) "
            "WITH c, row "
            f"CALL db.create.setVectorProperty(c, "
            f"'{self.embedding_node_property}', row.embedding) "
            "YIELD node "
            f"SET c.`{self.text_node_property}` = row.text "
            "SET c += row.metadata } IN TRANSACTIONS OF 1000 ROWS"
        )

        parameters = {
            "data": [
                {"text": text, "metadata": metadata, "embedding": embedding, "id": id}
                for text, metadata, embedding, id in zip(
                    texts, metadatas, embeddings, ids
                )
            ]
        }

        self.query(import_query, params=parameters)

        return ids

    def add_texts(
        self,
        texts: Iterable[str],
        metadatas: Optional[List[dict]] = None,
        ids: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> List[str]:
        """Run more texts through the embeddings and add to the vectorstore.

        Args:
            texts: Iterable of strings to add to the vectorstore.
            metadatas: Optional list of metadatas associated with the texts.
            kwargs: vectorstore specific parameters

        Returns:
            List of ids from adding the texts into the vectorstore.
        """
        embeddings = self.embedding.embed_documents(list(texts))
        return self.add_embeddings(
            texts=texts, embeddings=embeddings, metadatas=metadatas, ids=ids, **kwargs
        )

    def similarity_search(
        self,
        query: str,
        k: int = 4,
        **kwargs: Any,
    ) -> List[Document]:
        """Run similarity search with Neo4jVector.

        Args:
            query (str): Query text to search for.
            k (int): Number of results to return. Defaults to 4.

        Returns:
            List of Documents most similar to the query.
        """
        embedding = self.embedding.embed_query(text=query)
        return self.similarity_search_by_vector(
            embedding=embedding,
            k=k,
            query=query,
        )

    def similarity_search_with_score(
        self, query: str, k: int = 4
    ) -> List[Tuple[Document, float]]:
        """Return docs most similar to query.

        Args:
            query: Text to look up documents similar to.
            k: Number of Documents to return. Defaults to 4.

        Returns:
            List of Documents most similar to the query and score for each
        """
        embedding = self.embedding.embed_query(query)
        docs = self.similarity_search_with_score_by_vector(
            embedding=embedding, k=k, query=query
        )
        return docs

    def similarity_search_with_score_by_vector(
        self, embedding: List[float], k: int = 4, **kwargs: Any
    ) -> List[Tuple[Document, float]]:
        """
        Perform a similarity search in the Neo4j database using a
        given vector and return the top k similar documents with their scores.

        This method uses a Cypher query to find the top k documents that
        are most similar to a given embedding. The similarity is measured
        using a vector index in the Neo4j database. The results are returned
        as a list of tuples, each containing a Document object and
        its similarity score.

        Args:
            embedding (List[float]): The embedding vector to compare against.
            k (int, optional): The number of top similar documents to retrieve.

        Returns:
            List[Tuple[Document, float]]: A list of tuples, each containing
                                a Document object and its similarity score.
        """
        default_retrieval = (
            f"RETURN node.`{self.text_node_property}` AS text, score, "
            f"node {{.*, `{self.text_node_property}`: Null, "
            f"`{self.embedding_node_property}`: Null, id: Null }} AS metadata"
        )

        retrieval_query = (
            self.retrieval_query if self.retrieval_query else default_retrieval
        )

        read_query = _get_search_index_query(self.search_type) + retrieval_query
        parameters = {
            "index": self.index_name,
            "k": k,
            "embedding": embedding,
            "keyword_index": self.keyword_index_name,
            "query": kwargs["query"],
        }

        results = self.query(read_query, params=parameters)

        docs = [
            (
                Document(
                    page_content=result["text"],
                    metadata={
                        k: v for k, v in result["metadata"].items() if v is not None
                    },
                ),
                result["score"],
            )
            for result in results
        ]
        return docs

    def similarity_search_by_vector(
        self,
        embedding: List[float],
        k: int = 4,
        **kwargs: Any,
    ) -> List[Document]:
        """Return docs most similar to embedding vector.

        Args:
            embedding: Embedding to look up documents similar to.
            k: Number of Documents to return. Defaults to 4.

        Returns:
            List of Documents most similar to the query vector.
        """
        docs_and_scores = self.similarity_search_with_score_by_vector(
            embedding=embedding, k=k, **kwargs
        )
        return [doc for doc, _ in docs_and_scores]

    @classmethod
    def from_texts(
        cls: Type[Neo4jVector],
        texts: List[str],
        embedding: Embeddings,
        metadatas: Optional[List[dict]] = None,
        distance_strategy: DistanceStrategy = DEFAULT_DISTANCE_STRATEGY,
        ids: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> Neo4jVector:
        """
        Return Neo4jVector initialized from texts and embeddings.
        Neo4j credentials are required in the form of `url`, `username`,
        and `password` and optional `database` parameters.
        """
        embeddings = embedding.embed_documents(list(texts))

        return cls.__from(
            texts,
            embeddings,
            embedding,
            metadatas=metadatas,
            ids=ids,
            distance_strategy=distance_strategy,
            **kwargs,
        )

    @classmethod
    def from_embeddings(
        cls,
        text_embeddings: List[Tuple[str, List[float]]],
        embedding: Embeddings,
        metadatas: Optional[List[dict]] = None,
        distance_strategy: DistanceStrategy = DEFAULT_DISTANCE_STRATEGY,
        ids: Optional[List[str]] = None,
        pre_delete_collection: bool = False,
        **kwargs: Any,
    ) -> Neo4jVector:
        """Construct Neo4jVector wrapper from raw documents and pre-
        generated embeddings.

        Return Neo4jVector initialized from documents and embeddings.
        Neo4j credentials are required in the form of `url`, `username`,
        and `password` and optional `database` parameters.

        Example:
            .. code-block:: python

                from promptmanager.script.base.vectorstores.neo4j_vector import Neo4jVector
                from promptmanager.script.base.embeddings import OpenAIEmbeddings
                embeddings = OpenAIEmbeddings()
                text_embeddings = embeddings.embed_documents(texts)
                text_embedding_pairs = list(zip(texts, text_embeddings))
                vectorstore = Neo4jVector.from_embeddings(
                    text_embedding_pairs, embeddings)
        """
        texts = [t[0] for t in text_embeddings]
        embeddings = [t[1] for t in text_embeddings]

        return cls.__from(
            texts,
            embeddings,
            embedding,
            metadatas=metadatas,
            ids=ids,
            distance_strategy=distance_strategy,
            pre_delete_collection=pre_delete_collection,
            **kwargs,
        )

    @classmethod
    def from_existing_index(
        cls: Type[Neo4jVector],
        embedding: Embeddings,
        index_name: str,
        search_type: SearchType = DEFAULT_SEARCH_TYPE,
        keyword_index_name: Optional[str] = None,
        **kwargs: Any,
    ) -> Neo4jVector:
        """
        Get instance of an existing Neo4j vector index. This method will
        return the instance of the store without inserting any new
        embeddings.
        Neo4j credentials are required in the form of `url`, `username`,
        and `password` and optional `database` parameters along with
        the `index_name` definition.
        """

        if search_type == SearchType.HYBRID and not keyword_index_name:
            raise ValueError(
                "keyword_index name has to be specified "
                "when using hybrid search option"
            )

        store = cls(
            embedding=embedding,
            index_name=index_name,
            keyword_index_name=keyword_index_name,
            search_type=search_type,
            **kwargs,
        )

        embedding_dimension = store.retrieve_existing_index()

        if not embedding_dimension:
            raise ValueError(
                "The specified vector index name does not exist. "
                "Make sure to check if you spelled it correctly"
            )

        # Check if embedding function and vector index dimensions match
        if not store.embedding_dimension == embedding_dimension:
            raise ValueError(
                "The provided embedding function and vector index "
                "dimensions do not match.\n"
                f"Embedding function dimension: {store.embedding_dimension}\n"
                f"Vector index dimension: {embedding_dimension}"
            )

        if search_type == SearchType.HYBRID:
            fts_node_label = store.retrieve_existing_fts_index()
            # If the FTS index doesn't exist yet
            if not fts_node_label:
                raise ValueError(
                    "The specified keyword index name does not exist. "
                    "Make sure to check if you spelled it correctly"
                )
            else:  # Validate that FTS and Vector index use the same information
                if not fts_node_label == store.node_label:
                    raise ValueError(
                        "Vector and keyword index don't index the same node label"
                    )

        return store

    @classmethod
    def from_documents(
        cls: Type[Neo4jVector],
        documents: List[Document],
        embedding: Embeddings,
        distance_strategy: DistanceStrategy = DEFAULT_DISTANCE_STRATEGY,
        ids: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> Neo4jVector:
        """
        Return Neo4jVector initialized from documents and embeddings.
        Neo4j credentials are required in the form of `url`, `username`,
        and `password` and optional `database` parameters.
        """

        texts = [d.page_content for d in documents]
        metadatas = [d.metadata for d in documents]

        return cls.from_texts(
            texts=texts,
            embedding=embedding,
            distance_strategy=distance_strategy,
            metadatas=metadatas,
            ids=ids,
            **kwargs,
        )

    @classmethod
    def from_existing_graph(
        cls: Type[Neo4jVector],
        embedding: Embeddings,
        node_label: str,
        embedding_node_property: str,
        text_node_properties: List[str],
        *,
        keyword_index_name: Optional[str] = "keyword",
        index_name: str = "vector",
        search_type: SearchType = DEFAULT_SEARCH_TYPE,
        retrieval_query: str = "",
        **kwargs: Any,
    ) -> Neo4jVector:
        """
        Initialize and return a Neo4jVector instance from an existing graph.

        This method initializes a Neo4jVector instance using the provided
        parameters and the existing graph. It validates the existence of
        the indices and creates new ones if they don't exist.

        Returns:
        Neo4jVector: An instance of Neo4jVector initialized with the provided parameters
                    and existing graph.

        Example:
        >>> neo4j_vector = Neo4jVector.from_existing_graph(
        ...     embedding=my_embedding,
        ...     node_label="Document",
        ...     embedding_node_property="embedding",
        ...     text_node_properties=["title", "content"]
        ... )

        Note:
        Neo4j credentials are required in the form of `url`, `username`, and `password`,
        and optional `database` parameters passed as additional keyword arguments.
        """
        # Validate the list is not empty
        if not text_node_properties:
            raise ValueError(
                "Parameter `text_node_properties` must not be an empty list"
            )
        # Prefer retrieval query from params, otherwise construct it
        if not retrieval_query:
            retrieval_query = (
                f"RETURN reduce(str='', k IN {text_node_properties} |"
                " str + '\\n' + k + ': ' + coalesce(node[k], '')) AS text, "
                "node {.*, `"
                + embedding_node_property
                + "`: Null, id: Null, "
                + ", ".join([f"`{prop}`: Null" for prop in text_node_properties])
                + "} AS metadata, score"
            )
        store = cls(
            embedding=embedding,
            index_name=index_name,
            keyword_index_name=keyword_index_name,
            search_type=search_type,
            retrieval_query=retrieval_query,
            node_label=node_label,
            embedding_node_property=embedding_node_property,
            **kwargs,
        )

        # Check if the vector index already exists
        embedding_dimension = store.retrieve_existing_index()

        # If the vector index doesn't exist yet
        if not embedding_dimension:
            store.create_new_index()
        # If the index already exists, check if embedding dimensions match
        elif not store.embedding_dimension == embedding_dimension:
            raise ValueError(
                f"Index with name {store.index_name} already exists."
                "The provided embedding function and vector index "
                "dimensions do not match.\n"
                f"Embedding function dimension: {store.embedding_dimension}\n"
                f"Vector index dimension: {embedding_dimension}"
            )
        # FTS index for Hybrid search
        if search_type == SearchType.HYBRID:
            fts_node_label = store.retrieve_existing_fts_index(text_node_properties)
            # If the FTS index doesn't exist yet
            if not fts_node_label:
                store.create_new_keyword_index(text_node_properties)
            else:  # Validate that FTS and Vector index use the same information
                if not fts_node_label == store.node_label:
                    raise ValueError(
                        "Vector and keyword index don't index the same node label"
                    )

        # Populate embeddings
        while True:
            fetch_query = (
                f"MATCH (n:`{node_label}`) "
                f"WHERE n.{embedding_node_property} IS null "
                "AND any(k in $props WHERE n[k] IS NOT null) "
                f"RETURN elementId(n) AS id, reduce(str='',"
                "k IN $props | str + '\\n' + k + ':' + coalesce(n[k], '')) AS text "
                "LIMIT 1000"
            )
            data = store.query(fetch_query, params={"props": text_node_properties})
            text_embeddings = embedding.embed_documents([el["text"] for el in data])

            params = {
                "data": [
                    {"id": el["id"], "embedding": embedding}
                    for el, embedding in zip(data, text_embeddings)
                ]
            }

            store.query(
                "UNWIND $data AS row "
                f"MATCH (n:`{node_label}`) "
                "WHERE elementId(n) = row.id "
                f"CALL db.create.setVectorProperty(n, "
                f"'{embedding_node_property}', row.embedding) "
                "YIELD node RETURN count(*)",
                params=params,
            )
            # If embedding calculation should be stopped
            if len(data) < 1000:
                break
        return store

    def _select_relevance_score_fn(self) -> Callable[[float], float]:
        """
        The 'correct' relevance function
        may differ depending on a few things, including:
        - the distance / similarity metric used by the VectorStore
        - the scale of your embeddings (OpenAI's are unit normed. Many others are not!)
        - embedding dimensionality
        - etc.
        """
        if self.override_relevance_score_fn is not None:
            return self.override_relevance_score_fn

        # Default strategy is to rely on distance strategy provided
        # in vectorstore constructor
        if self._distance_strategy == DistanceStrategy.COSINE:
            return lambda x: x
        elif self._distance_strategy == DistanceStrategy.EUCLIDEAN_DISTANCE:
            return lambda x: x
        else:
            raise ValueError(
                "No supported normalization function"
                f" for distance_strategy of {self._distance_strategy}."
                "Consider providing relevance_score_fn to PGVector constructor."
            )
