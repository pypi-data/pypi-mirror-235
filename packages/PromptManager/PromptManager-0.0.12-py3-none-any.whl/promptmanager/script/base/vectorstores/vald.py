"""Wrapper around Vald vector database."""
from __future__ import annotations

from typing import Any, Iterable, List, Optional, Tuple, Type

import numpy as np

from promptmanager.script.base.docstore.document import Document
from promptmanager.script.base.schema.embeddings import Embeddings
from promptmanager.script.base.schema.vectorstore import PMVectorDB
from promptmanager.script.base.vectorstores.utils import maximal_marginal_relevance


class Vald(PMVectorDB):
    """Wrapper around Vald vector database.

    To use, you should have the ``vald-client-python`` python package installed.

    Example:
        .. code-block:: python

            from promptmanager.script.base.embeddings import HuggingFaceEmbeddings
            from promptmanager.script.base.vectorstores import Vald

            texts = ['foo', 'bar', 'baz']
            vald = Vald.from_texts(
                texts=texts,
                embedding=HuggingFaceEmbeddings(),
                host="localhost",
                port=8080,
                skip_strict_exist_check=False,
             )
    """

    def __init__(
        self,
        embedding: Embeddings,
        host: str = "localhost",
        port: int = 8080,
        grpc_options: Tuple = (
            ("grpc.keepalive_time_ms", 1000 * 10),
            ("grpc.keepalive_timeout_ms", 1000 * 10),
        ),
    ):
        self._embedding = embedding
        self.target = host + ":" + str(port)
        self.grpc_options = grpc_options

    @property
    def embeddings(self) -> Optional[Embeddings]:
        return self._embedding

    def add_texts(
        self,
        texts: Iterable[str],
        metadatas: Optional[List[dict]] = None,
        skip_strict_exist_check: bool = False,
        **kwargs: Any,
    ) -> List[str]:
        """
        Args:
            skip_strict_exist_check: Deprecated. This is not used basically.
        """
        try:
            import grpc
            from vald.v1.payload import payload_pb2
            from vald.v1.vald import upsert_pb2_grpc
        except ImportError:
            raise ValueError(
                "Could not import vald-client-python python package. "
                "Please install it with `pip install vald-client-python`."
            )

        channel = grpc.insecure_channel(self.target, options=self.grpc_options)
        # Depending on the network quality,
        # it is necessary to wait for ChannelConnectivity.READY.
        # _ = grpc.channel_ready_future(channel).result(timeout=10)
        stub = upsert_pb2_grpc.UpsertStub(channel)
        cfg = payload_pb2.Upsert.Config(skip_strict_exist_check=skip_strict_exist_check)

        ids = []
        embs = self._embedding.embed_documents(list(texts))
        for text, emb in zip(texts, embs):
            vec = payload_pb2.Object.Vector(id=text, vector=emb)
            res = stub.Upsert(payload_pb2.Upsert.Request(vector=vec, config=cfg))
            ids.append(res.uuid)

        channel.close()
        return ids

    def delete(
        self,
        ids: Optional[List[str]] = None,
        skip_strict_exist_check: bool = False,
        **kwargs: Any,
    ) -> Optional[bool]:
        """
        Args:
            skip_strict_exist_check: Deprecated. This is not used basically.
        """
        try:
            import grpc
            from vald.v1.payload import payload_pb2
            from vald.v1.vald import remove_pb2_grpc
        except ImportError:
            raise ValueError(
                "Could not import vald-client-python python package. "
                "Please install it with `pip install vald-client-python`."
            )

        if ids is None:
            raise ValueError("No ids provided to delete")

        channel = grpc.insecure_channel(self.target, options=self.grpc_options)
        # Depending on the network quality,
        # it is necessary to wait for ChannelConnectivity.READY.
        # _ = grpc.channel_ready_future(channel).result(timeout=10)
        stub = remove_pb2_grpc.RemoveStub(channel)
        cfg = payload_pb2.Remove.Config(skip_strict_exist_check=skip_strict_exist_check)

        for _id in ids:
            oid = payload_pb2.Object.ID(id=_id)
            _ = stub.Remove(payload_pb2.Remove.Request(id=oid, config=cfg))

        channel.close()
        return True

    def similarity_search(
        self,
        query: str,
        k: int = 4,
        radius: float = -1.0,
        epsilon: float = 0.01,
        timeout: int = 3000000000,
        **kwargs: Any,
    ) -> List[Document]:
        docs_and_scores = self.similarity_search_with_score(
            query, k, radius, epsilon, timeout
        )

        docs = []
        for doc, _ in docs_and_scores:
            docs.append(doc)

        return docs

    def similarity_search_with_score(
        self,
        query: str,
        k: int = 4,
        radius: float = -1.0,
        epsilon: float = 0.01,
        timeout: int = 3000000000,
        **kwargs: Any,
    ) -> List[Tuple[Document, float]]:
        emb = self._embedding.embed_query(query)
        docs_and_scores = self.similarity_search_with_score_by_vector(
            emb, k, radius, epsilon, timeout
        )

        return docs_and_scores

    def similarity_search_by_vector(
        self,
        embedding: List[float],
        k: int = 4,
        radius: float = -1.0,
        epsilon: float = 0.01,
        timeout: int = 3000000000,
        **kwargs: Any,
    ) -> List[Document]:
        docs_and_scores = self.similarity_search_with_score_by_vector(
            embedding, k, radius, epsilon, timeout
        )

        docs = []
        for doc, _ in docs_and_scores:
            docs.append(doc)

        return docs

    def similarity_search_with_score_by_vector(
        self,
        embedding: List[float],
        k: int = 4,
        radius: float = -1.0,
        epsilon: float = 0.01,
        timeout: int = 3000000000,
        **kwargs: Any,
    ) -> List[Tuple[Document, float]]:
        try:
            import grpc
            from vald.v1.payload import payload_pb2
            from vald.v1.vald import search_pb2_grpc
        except ImportError:
            raise ValueError(
                "Could not import vald-client-python python package. "
                "Please install it with `pip install vald-client-python`."
            )

        channel = grpc.insecure_channel(self.target, options=self.grpc_options)
        # Depending on the network quality,
        # it is necessary to wait for ChannelConnectivity.READY.
        # _ = grpc.channel_ready_future(channel).result(timeout=10)
        stub = search_pb2_grpc.SearchStub(channel)
        cfg = payload_pb2.Search.Config(
            num=k, radius=radius, epsilon=epsilon, timeout=timeout
        )

        res = stub.Search(payload_pb2.Search.Request(vector=embedding, config=cfg))

        docs_and_scores = []
        for result in res.results:
            docs_and_scores.append((Document(page_content=result.id), result.distance))

        channel.close()
        return docs_and_scores

    def max_marginal_relevance_search(
        self,
        query: str,
        k: int = 4,
        fetch_k: int = 20,
        lambda_mult: float = 0.5,
        radius: float = -1.0,
        epsilon: float = 0.01,
        timeout: int = 3000000000,
        **kwargs: Any,
    ) -> List[Document]:
        emb = self._embedding.embed_query(query)
        docs = self.max_marginal_relevance_search_by_vector(
            emb,
            k=k,
            fetch_k=fetch_k,
            radius=radius,
            epsilon=epsilon,
            timeout=timeout,
            lambda_mult=lambda_mult,
        )

        return docs

    def max_marginal_relevance_search_by_vector(
        self,
        embedding: List[float],
        k: int = 4,
        fetch_k: int = 20,
        lambda_mult: float = 0.5,
        radius: float = -1.0,
        epsilon: float = 0.01,
        timeout: int = 3000000000,
        **kwargs: Any,
    ) -> List[Document]:
        try:
            import grpc
            from vald.v1.payload import payload_pb2
            from vald.v1.vald import object_pb2_grpc
        except ImportError:
            raise ValueError(
                "Could not import vald-client-python python package. "
                "Please install it with `pip install vald-client-python`."
            )

        channel = grpc.insecure_channel(self.target, options=self.grpc_options)
        # Depending on the network quality,
        # it is necessary to wait for ChannelConnectivity.READY.
        # _ = grpc.channel_ready_future(channel).result(timeout=10)
        stub = object_pb2_grpc.ObjectStub(channel)

        docs_and_scores = self.similarity_search_with_score_by_vector(
            embedding, fetch_k=fetch_k, radius=radius, epsilon=epsilon, timeout=timeout
        )

        docs = []
        embs = []
        for doc, _ in docs_and_scores:
            vec = stub.GetObject(
                payload_pb2.Object.VectorRequest(
                    id=payload_pb2.Object.ID(id=doc.page_content)
                )
            )
            embs.append(vec.vector)
            docs.append(doc)

        mmr = maximal_marginal_relevance(
            np.array(embedding),
            embs,
            lambda_mult=lambda_mult,
            k=k,
        )

        channel.close()
        return [docs[i] for i in mmr]

    @classmethod
    def from_texts(
        cls: Type[Vald],
        texts: List[str],
        embedding: Embeddings,
        metadatas: Optional[List[dict]] = None,
        host: str = "localhost",
        port: int = 8080,
        grpc_options: Tuple = (
            ("grpc.keepalive_time_ms", 1000 * 10),
            ("grpc.keepalive_timeout_ms", 1000 * 10),
        ),
        skip_strict_exist_check: bool = False,
        **kwargs: Any,
    ) -> Vald:
        """
        Args:
            skip_strict_exist_check: Deprecated. This is not used basically.
        """
        vald = cls(
            embedding=embedding,
            host=host,
            port=port,
            grpc_options=grpc_options,
            **kwargs,
        )
        vald.add_texts(
            texts=texts,
            metadatas=metadatas,
            skip_strict_exist_check=skip_strict_exist_check,
        )
        return vald


"""We will support if there are any requests."""
#    async def aadd_texts(
#        self,
#        texts: Iterable[str],
#        metadatas: Optional[List[dict]] = None,
#        **kwargs: Any,
#    ) -> List[str]:
#        pass
#
#    def _select_relevance_score_fn(self) -> Callable[[float], float]:
#        pass
#
#    def _similarity_search_with_relevance_scores(
#        self,
#        query: str,
#        k: int = 4,
#        **kwargs: Any,
#    ) -> List[Tuple[Document, float]]:
#        pass
#
#    def similarity_search_with_relevance_scores(
#        self,
#        query: str,
#        k: int = 4,
#        **kwargs: Any,
#    ) -> List[Tuple[Document, float]]:
#        pass
#
#    async def amax_marginal_relevance_search_by_vector(
#        self,
#        embedding: List[float],
#        k: int = 4,
#        fetch_k: int = 20,
#        lambda_mult: float = 0.5,
#        **kwargs: Any,
#    ) -> List[Document]:
#        pass
#
#    @classmethod
#    async def afrom_texts(
#        cls: Type[VST],
#        texts: List[str],
#        embedding: Embeddings,
#        metadatas: Optional[List[dict]] = None,
#        **kwargs: Any,
#    ) -> VST:
#        pass
