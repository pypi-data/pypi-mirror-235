import logging

import time
import uuid

import chromadb
from chromadb.api.models import Collection
from chromadb.utils import embedding_functions

from promptmanager.runtime.flow import PMNodeOutput
from promptmanager.script.base.schema import Document
from promptmanager.script.base.text_splitter import CharacterTextSplitter

OPENAI_API_KEY = 'OPENAI_API_KEY'
logger = logging.getLogger('pm_log')


class ChromaWriter:
    def __init__(self, connection_type, host=None, port=None, collection=None):
        self.connection_type = connection_type
        self.host = host
        self.port = port
        self.collection = collection

    def exec(self, documents: list[Document] = None) -> Collection:

        # from promptmanager.script.base.embeddings import OpenAIEmbeddings
        # embeddings = OpenAIEmbeddings()
        # new_client = chromadb.EphemeralClient()
        # from promptmanager.script.base.vectorstores.chroma import Chroma
        # openai_lc_client = Chroma.from_documents(
        #     docs, embeddings, client=new_client, collection_name="openai_collection"
        # )
        # openai_lc_client.add_documents()
        #
        # query = "What did the president say about Ketanji Brown Jackson"
        # docs = openai_lc_client.similarity_search(query)
        # print(docs[0].page_content)

        if self.connection_type == 'local':
            # local chromadb
            persistent_client = chromadb.PersistentClient()
            collection = persistent_client.get_or_create_collection(self.collection)
        else:
            # remote chromadb
            client = chromadb.HttpClient(host=self.host, port=self.port)
            emb_fn = embedding_functions.ONNXMiniLM_L6_V2()
            try:
                collection = client.create_collection(name=self.collection, embedding_function=emb_fn)
            except Exception:
                collection = client.get_collection(name=self.collection, embedding_function=emb_fn)

        # add documents
        for doc in documents:
            collection.add(
                ids=[str(uuid.uuid1())], metadatas=doc.metadata, documents=doc.page_content
            )

        return collection


def run(params: dict, inputs: dict, outputs: dict) -> PMNodeOutput:
    logger.info("Welcome to Use Chroma Writer!")

    logger.info("This is params info:")
    logger.info(params)
    logger.info("This is inputs info:")
    logger.info(inputs)
    logger.info("This is outputs info:")
    logger.info(outputs)

    connection_type = params['script']['connection_type']['value']
    host = params['script']['Host']['value']
    port = params['script']['Port']['value']
    collection = params['script']['Collection']['value']

    documents = inputs['documents']['value']

    logger.info("To write from chroma db:")
    chroma_writer = ChromaWriter(connection_type=connection_type, host=host, port=port, collection=collection)
    results = chroma_writer.exec(documents=documents)

    output = PMNodeOutput()
    for output_name in outputs.keys():
        output.add_output(output_name, results)

    return output
