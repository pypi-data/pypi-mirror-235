"""
Question answering over an RDF or OWL graph using SPARQL.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from promptmanager.script.base.callbacks.manager import CallbackManagerForChainRun
from promptmanager.script.base.chains.base import Chain
from promptmanager.script.base.chains.graph_qa.prompts import (
    SPARQL_GENERATION_SELECT_PROMPT,
    SPARQL_GENERATION_UPDATE_PROMPT,
    SPARQL_INTENT_PROMPT,
    SPARQL_QA_PROMPT,
)
from promptmanager.script.base.chains.llm import LLMChain
from promptmanager.script.base.graphs.rdf_graph import RdfGraph
from promptmanager.script.base.prompts.base import BasePromptTemplate
from promptmanager.script.base.pydantic_v1 import Field
from promptmanager.script.base.schema.language_model import BaseLanguageModel


class GraphSparqlQAChain(Chain):
    """
    Chain for question-answering against an RDF or OWL graph by generating
    SPARQL statements.
    """

    graph: RdfGraph = Field(exclude=True)
    sparql_generation_select_chain: LLMChain
    sparql_generation_update_chain: LLMChain
    sparql_intent_chain: LLMChain
    qa_chain: LLMChain
    input_key: str = "query"  #: :meta private:
    output_key: str = "result"  #: :meta private:

    @property
    def input_keys(self) -> List[str]:
        return [self.input_key]

    @property
    def output_keys(self) -> List[str]:
        _output_keys = [self.output_key]
        return _output_keys

    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        *,
        qa_prompt: BasePromptTemplate = SPARQL_QA_PROMPT,
        sparql_select_prompt: BasePromptTemplate = SPARQL_GENERATION_SELECT_PROMPT,
        sparql_update_prompt: BasePromptTemplate = SPARQL_GENERATION_UPDATE_PROMPT,
        sparql_intent_prompt: BasePromptTemplate = SPARQL_INTENT_PROMPT,
        **kwargs: Any,
    ) -> GraphSparqlQAChain:
        """Initialize from LLM."""
        qa_chain = LLMChain(llm=llm, prompt=qa_prompt)
        sparql_generation_select_chain = LLMChain(llm=llm, prompt=sparql_select_prompt)
        sparql_generation_update_chain = LLMChain(llm=llm, prompt=sparql_update_prompt)
        sparql_intent_chain = LLMChain(llm=llm, prompt=sparql_intent_prompt)

        return cls(
            qa_chain=qa_chain,
            sparql_generation_select_chain=sparql_generation_select_chain,
            sparql_generation_update_chain=sparql_generation_update_chain,
            sparql_intent_chain=sparql_intent_chain,
            **kwargs,
        )

    def _call(
        self,
        inputs: Dict[str, Any],
        run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, str]:
        """
        Generate SPARQL query, use it to retrieve a response from the gdb and answer
        the question.
        """
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        callbacks = _run_manager.get_child()
        prompt = inputs[self.input_key]

        _intent = self.sparql_intent_chain.run({"prompt": prompt}, callbacks=callbacks)
        intent = _intent.strip()

        if "SELECT" in intent and "UPDATE" not in intent:
            sparql_generation_chain = self.sparql_generation_select_chain
            intent = "SELECT"
        elif "UPDATE" in intent and "SELECT" not in intent:
            sparql_generation_chain = self.sparql_generation_update_chain
            intent = "UPDATE"
        else:
            raise ValueError(
                "I am sorry, but this prompt seems to fit none of the currently "
                "supported SPARQL query types, i.e., SELECT and UPDATE."
            )

        _run_manager.on_text("Identified intent:", end="\n", verbose=self.verbose)
        _run_manager.on_text(intent, color="green", end="\n", verbose=self.verbose)

        generated_sparql = sparql_generation_chain.run(
            {"prompt": prompt, "schema": self.graph.get_schema}, callbacks=callbacks
        )

        _run_manager.on_text("Generated SPARQL:", end="\n", verbose=self.verbose)
        _run_manager.on_text(
            generated_sparql, color="green", end="\n", verbose=self.verbose
        )

        if intent == "SELECT":
            context = self.graph.query(generated_sparql)

            _run_manager.on_text("Full Context:", end="\n", verbose=self.verbose)
            _run_manager.on_text(
                str(context), color="green", end="\n", verbose=self.verbose
            )
            result = self.qa_chain(
                {"prompt": prompt, "context": context},
                callbacks=callbacks,
            )
            res = result[self.qa_chain.output_key]
        elif intent == "UPDATE":
            self.graph.update(generated_sparql)
            res = "Successfully inserted triples into the graph."
        else:
            raise ValueError("Unsupported SPARQL query type.")
        return {self.output_key: res}
