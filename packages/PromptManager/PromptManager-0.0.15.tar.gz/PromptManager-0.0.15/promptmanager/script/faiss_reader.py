import logging
import os

from promptmanager.runtime.flow import PMNodeOutput
from promptmanager.script.base.schema import Document
from promptmanager.script.base.schema.vectorstore import PMVectorDB
from promptmanager.script.base.text_splitter import CharacterTextSplitter
from promptmanager.script.base.vectorstores.faiss import FAISS

logger = logging.getLogger('pm_log')

OPENAI_API_KEY = 'OPENAI_API_KEY'


class FaissReader:
    def __init__(self,
                 openai_api_key,
                 documents: list[Document] = None,
                 embeddings=None,
                 vectorstore: PMVectorDB = None):
        self.openai_api_key = openai_api_key
        self.documents = documents
        self.embeddings = embeddings
        self.vectorstore = vectorstore

    def exec(self, query_text):
        os.environ[OPENAI_API_KEY] = self.openai_api_key

        vectorstore = self.vectorstore
        if not vectorstore:
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            docs = text_splitter.split_documents(self.documents)
            # embeddings = OpenAIEmbeddings()
            vectorstore = FAISS.from_documents(docs, self.embeddings)

        result = vectorstore.similarity_search(query_text)

        logger.info(result)

        result_str_list = []
        for i, d in enumerate(result):
            result_str_list.append(d.page_content)

        return result_str_list


def run(params: dict = None, inputs: dict = None, outputs=None) -> PMNodeOutput:
    logger.info("Welcome to Faiss Reader!")
    logger.info("This is params info:")
    logger.info(params)
    logger.info("This is inputs info:")
    logger.info(inputs)
    logger.info("This is outputs info:")
    logger.info(outputs)

    openai_api_key = params['script']['openai_api_key']['value']

    documents = inputs['documents']['value']
    embeddings = inputs['embeddings']['value']
    vectorstore = inputs['vectorstore']['value']
    query_text = inputs['query_text']['value']

    faiss_reader = FaissReader(openai_api_key=openai_api_key, documents=documents, embeddings=embeddings,
                               vectorstore=vectorstore)
    result = faiss_reader.exec(query_text)

    output = PMNodeOutput()
    for output_name in outputs.keys():
        output.add_output(output_name, result)

    return output
