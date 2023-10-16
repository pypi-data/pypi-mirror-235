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


class DingoDBWriter:
    def __init__(self, host, port, user, password, embeddings):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.embeddings = embeddings

    def exec(self, text_key, index_name, documents: list[Document] = None):
        from dingodb import DingoDB
        dingo_client = DingoDB(user=self.user, password=self.password, host=[self.host + ":" + self.port])
        if index_name not in dingo_client.get_index():
            dingo_client.create_index(
                index_name=index_name,
                dimension=1024,
                metric_type='cosine',
                auto_id=False
            )
        # First, check if our index already exists. If it doesn't, we create it
        # if index_name not in dingo_client.get_index():
        #     # we create a new index, modify to your own
        #     dingo_client.create_index(
        #         index_name=index_name,
        #         dimension=1024,
        #         metric_type='cosine',
        #         auto_id=False
        #     )
        # from promptmanager.script.base.embeddings.huggingface import HuggingFaceEmbeddings
        # model_name = "GanymedeNil/text2vec-large-chinese"
        ###向量化工具
        # embeddings = HuggingFaceEmbeddings(model_name=model_name, model_kwargs={'device': "cuda"})
        # embeddings = HuggingFaceEmbeddings(model_name=model_name, model_kwargs={'device': "cpu"})  # 换成cpu也行

        from promptmanager.script.base.vectorstores import Dingo
        vectorstore = Dingo(self.embeddings, text_key, client=dingo_client, index_name=index_name)

        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)
        for doc in docs:
            vectorstore.add_texts(texts=doc.page_content, text_key=text_key)

        return vectorstore


def run(params: dict, inputs: dict, outputs: dict) -> PMNodeOutput:
    logger.info("Welcome to Use DingoDB Writer!")

    logger.info("This is params info:")
    logger.info(params)
    logger.info("This is inputs info:")
    logger.info(inputs)
    logger.info("This is outputs info:")
    logger.info(outputs)

    connection_type = params['script']['connection_type']['value']
    host = params['script']['Host']['value']
    port = params['script']['Port']['value']
    index_name = params['script']['Index']['value']
    user = params['script']['user']['value']
    password = params['script']['password']['value']
    text_key = params['script']['text_key']['value']

    query_text = inputs['query_text']['value']
    embeddings = inputs['embeddings']['value']

    documents = inputs['documents']['value']

    logger.info("To write from dingodb:")
    dingodb_writer = DingoDBWriter(connection_type=connection_type, host=host, port=port, collection=collection)
    results = dingodb_writer.exec(documents=documents)

    output = PMNodeOutput()
    for output_name in outputs.keys():
        output.add_output(output_name, results)

    return output
