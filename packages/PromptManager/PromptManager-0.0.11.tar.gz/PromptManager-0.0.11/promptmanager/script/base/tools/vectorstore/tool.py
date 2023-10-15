"""Tools for interacting with vectorstores."""

import json
from typing import Any, Dict, Optional

from promptmanager.script.base.callbacks.manager import CallbackManagerForToolRun
from promptmanager.script.base.llms.openai import OpenAI
from promptmanager.script.base.pydantic_v1 import BaseModel, Field
from promptmanager.script.base.schema.language_model import BaseLanguageModel
from promptmanager.script.base.schema.vectorstore import VectorStore
from promptmanager.script.base.tools.base import BaseTool


class BaseVectorStoreTool(BaseModel):
    """Base class for tools that use a VectorStore."""

    vectorstore: VectorStore = Field(exclude=True)
    llm: BaseLanguageModel = Field(default_factory=lambda: OpenAI(temperature=0))

    class Config(BaseTool.Config):
        pass


def _create_description_from_template(values: Dict[str, Any]) -> Dict[str, Any]:
    values["description"] = values["template"].format(name=values["name"])
    return values


class VectorStoreQATool(BaseVectorStoreTool, BaseTool):
    """Tool for the VectorDBQA chain. To be initialized with name and chain."""

    @staticmethod
    def get_description(name: str, description: str) -> str:
        template: str = (
            "Useful for when you need to answer questions about {name}. "
            "Whenever you need information about {description} "
            "you should ALWAYS use this. "
            "Input should be a fully formed question."
        )
        return template.format(name=name, description=description)

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        from promptmanager.script.base.chains.retrieval_qa.base import RetrievalQA

        chain = RetrievalQA.from_chain_type(
            self.llm, retriever=self.vectorstore.as_retriever()
        )
        return chain.run(
            query, callbacks=run_manager.get_child() if run_manager else None
        )


class VectorStoreQAWithSourcesTool(BaseVectorStoreTool, BaseTool):
    """Tool for the VectorDBQAWithSources chain."""

    @staticmethod
    def get_description(name: str, description: str) -> str:
        template: str = (
            "Useful for when you need to answer questions about {name} and the sources "
            "used to construct the answer. "
            "Whenever you need information about {description} "
            "you should ALWAYS use this. "
            " Input should be a fully formed question. "
            "Output is a json serialized dictionary with keys `answer` and `sources`. "
            "Only use this tool if the user explicitly asks for sources."
        )
        return template.format(name=name, description=description)

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""

        from promptmanager.script.base.chains.qa_with_sources.retrieval import (
            RetrievalQAWithSourcesChain,
        )

        chain = RetrievalQAWithSourcesChain.from_chain_type(
            self.llm, retriever=self.vectorstore.as_retriever()
        )
        return json.dumps(
            chain(
                {chain.question_key: query},
                return_only_outputs=True,
                callbacks=run_manager.get_child() if run_manager else None,
            )
        )
