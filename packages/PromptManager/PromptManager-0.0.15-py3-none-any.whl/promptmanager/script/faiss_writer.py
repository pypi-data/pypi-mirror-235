import logging

import time

from promptmanager.runtime.flow import PMNodeOutput
from promptmanager.script.base.schema import Document
from promptmanager.script.base.schema.vectorstore import PMVectorDB
from promptmanager.script.base.text_splitter import CharacterTextSplitter
from promptmanager.script.base.vectorstores.faiss import FAISS

OPENAI_API_KEY = 'OPENAI_API_KEY'
logger = logging.getLogger('pm_log')


class FaissWriter:
    def __int__(self):
        pass

    def exec(self, documents: list[Document], embeddings) -> PMVectorDB:
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        # embeddings = OpenAIEmbeddings()

        vectorstore = FAISS.from_documents(docs, embeddings)

        index_name = "faiss_index_" + str(time.time())
        vectorstore.save_local(index_name)

        return vectorstore


def run(params: dict = None, inputs: dict = None, outputs=None) -> PMNodeOutput:
    logger.info("Welcome to Faiss Writer!")
    logger.info("This is params info:")
    logger.info(params)
    logger.info("This is inputs info:")
    logger.info(inputs)
    logger.info("This is outputs info:")
    logger.info(outputs)

    documents = inputs['documents']['value']
    embeddings = inputs['embeddings']['value']

    faiss_writer = FaissWriter()
    result = faiss_writer.exec(documents=documents, embeddings=embeddings)

    output = PMNodeOutput()
    for output_name in outputs.keys():
        output.add_output(output_name, result)

    return output
