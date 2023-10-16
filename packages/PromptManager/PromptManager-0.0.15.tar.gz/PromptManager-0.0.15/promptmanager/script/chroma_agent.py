import logging
import time

from promptmanager.runtime.flow import PMNodeOutput
from promptmanager.script.base.schema import Document

logger = logging.getLogger('pm_log')

OPENAI_API_KEY = "OPENAI_API_KEY"


class ChromaAgent:
    def __init__(self, model, openai_api_key, collection_name, embeddings):
        self.model = model
        self.openai_api_key = openai_api_key
        self.collection_name = collection_name
        self.embeddings = embeddings

    def exec(self, documents: list[Document], query_text) -> str:
        # from promptmanager.script.base.embeddings.openai import OpenAIEmbeddings
        from promptmanager.script.base.vectorstores import Chroma
        from promptmanager.script.base.text_splitter import CharacterTextSplitter
        # from promptmanager.script.base.llms import OpenAI
        # from promptmanager.script.base.chains import VectorDBQA

        import os
        os.environ[OPENAI_API_KEY] = self.openai_api_key

        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)

        # embeddings = OpenAIEmbeddings()
        # "state-of-union"
        state_of_union_store = Chroma.from_documents(
            texts, self.embeddings, collection_name=self.collection_name
        )

        from promptmanager.script.base.agents.agent_toolkits import (
            create_vectorstore_agent,
            VectorStoreToolkit,
            VectorStoreInfo,
        )

        vectorstore_name = "vectorstore_" + str(time.time())
        vectorstore_info = VectorStoreInfo(
            name=vectorstore_name,
            description=vectorstore_name,
            vectorstore=state_of_union_store,
        )
        toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)
        # llm = OpenAI(temperature=0)
        agent_executor = create_vectorstore_agent(llm=self.model, toolkit=toolkit, verbose=True)

        results = agent_executor.run(query_text)

        logger.info(results)

        return results


def run(params: dict = None, inputs: dict = None, outputs=None) -> PMNodeOutput:
    logger.info("Welcome to Use Chroma Agent!")
    logger.info("This is params info:")
    logger.info(params)
    logger.info("This is inputs info:")
    logger.info(inputs)
    logger.info("This is outputs info:")
    logger.info(outputs)

    collection_name = params['script']['Collection']['value']
    model = params['script']['model']['value']
    openai_api_key = params['script']['openai_api_key']['value']

    embeddings = inputs['embeddings']['value']
    documents = inputs['documents']['value']
    query_text = inputs['query_text']['value']

    chroma_agent = ChromaAgent(model=model, openai_api_key=openai_api_key, collection_name=collection_name,
                               embeddings=embeddings)
    result = chroma_agent.exec(documents=documents, query_text=query_text)

    output = PMNodeOutput()
    for output_name in outputs.keys():
        output.add_output(output_name, result)

    return output
