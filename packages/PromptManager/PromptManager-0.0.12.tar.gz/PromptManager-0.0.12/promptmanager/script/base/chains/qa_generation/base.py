from __future__ import annotations

import json
from typing import Any, Dict, List, Optional

from promptmanager.script.base.callbacks.manager import CallbackManagerForChainRun
from promptmanager.script.base.chains.base import Chain
from promptmanager.script.base.chains.llm import LLMChain
from promptmanager.script.base.chains.qa_generation.prompt import PROMPT_SELECTOR
from promptmanager.script.base.pydantic_v1 import Field
from promptmanager.script.base.schema import BasePromptTemplate
from promptmanager.script.base.schema.language_model import BaseLanguageModel
from promptmanager.script.base.text_splitter import RecursiveCharacterTextSplitter, TextSplitter


class QAGenerationChain(Chain):
    """Base class for question-answer generation chains."""

    llm_chain: LLMChain
    """LLM Chain that generates responses from user input and context."""
    text_splitter: TextSplitter = Field(
        default=RecursiveCharacterTextSplitter(chunk_overlap=500)
    )
    """Text splitter that splits the input into chunks."""
    input_key: str = "text"
    """Key of the input to the chain."""
    output_key: str = "questions"
    """Key of the output of the chain."""
    k: Optional[int] = None
    """Number of questions to generate."""

    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        prompt: Optional[BasePromptTemplate] = None,
        **kwargs: Any,
    ) -> QAGenerationChain:
        """
        Create a QAGenerationChain from a language model.

        Args:
            llm: a language model
            prompt: a prompt template
            **kwargs: additional arguments

        Returns:
            a QAGenerationChain class
        """
        _prompt = prompt or PROMPT_SELECTOR.get_prompt(llm)
        chain = LLMChain(llm=llm, prompt=_prompt)
        return cls(llm_chain=chain, **kwargs)

    @property
    def _chain_type(self) -> str:
        raise NotImplementedError

    @property
    def input_keys(self) -> List[str]:
        return [self.input_key]

    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]

    def _call(
        self,
        inputs: Dict[str, Any],
        run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, List]:
        docs = self.text_splitter.create_documents([inputs[self.input_key]])
        results = self.llm_chain.generate(
            [{"text": d.page_content} for d in docs], run_manager=run_manager
        )
        qa = [json.loads(res[0].text) for res in results.generations]
        return {self.output_key: qa}
