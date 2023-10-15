"""Use a single chain to route an input to one of multiple retrieval qa chains."""
from __future__ import annotations

from typing import Any, Dict, List, Mapping, Optional

from promptmanager.script.base.chains import ConversationChain
from promptmanager.script.base.chains.base import Chain
from promptmanager.script.base.chains.conversation.prompt import DEFAULT_TEMPLATE
from promptmanager.script.base.chains.retrieval_qa.base import BaseRetrievalQA, RetrievalQA
from promptmanager.script.base.chains.router.base import MultiRouteChain
from promptmanager.script.base.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from promptmanager.script.base.chains.router.multi_retrieval_prompt import (
    MULTI_RETRIEVAL_ROUTER_TEMPLATE,
)
from promptmanager.script.base.chat_models import ChatOpenAI
from promptmanager.script.base.prompts import PromptTemplate
from promptmanager.script.base.schema import BaseRetriever
from promptmanager.script.base.schema.language_model import BaseLanguageModel


class MultiRetrievalQAChain(MultiRouteChain):
    """A multi-route chain that uses an LLM router chain to choose amongst retrieval
    qa chains."""

    router_chain: LLMRouterChain
    """Chain for deciding a destination chain and the input to it."""
    destination_chains: Mapping[str, BaseRetrievalQA]
    """Map of name to candidate chains that inputs can be routed to."""
    default_chain: Chain
    """Default chain to use when router doesn't map input to one of the destinations."""

    @property
    def output_keys(self) -> List[str]:
        return ["result"]

    @classmethod
    def from_retrievers(
        cls,
        llm: BaseLanguageModel,
        retriever_infos: List[Dict[str, Any]],
        default_retriever: Optional[BaseRetriever] = None,
        default_prompt: Optional[PromptTemplate] = None,
        default_chain: Optional[Chain] = None,
        **kwargs: Any,
    ) -> MultiRetrievalQAChain:
        if default_prompt and not default_retriever:
            raise ValueError(
                "`default_retriever` must be specified if `default_prompt` is "
                "provided. Received only `default_prompt`."
            )
        destinations = [f"{r['name']}: {r['description']}" for r in retriever_infos]
        destinations_str = "\n".join(destinations)
        router_template = MULTI_RETRIEVAL_ROUTER_TEMPLATE.format(
            destinations=destinations_str
        )
        router_prompt = PromptTemplate(
            template=router_template,
            input_variables=["input"],
            output_parser=RouterOutputParser(next_inputs_inner_key="query"),
        )
        router_chain = LLMRouterChain.from_llm(llm, router_prompt)
        destination_chains = {}
        for r_info in retriever_infos:
            prompt = r_info.get("prompt")
            retriever = r_info["retriever"]
            chain = RetrievalQA.from_llm(llm, prompt=prompt, retriever=retriever)
            name = r_info["name"]
            destination_chains[name] = chain
        if default_chain:
            _default_chain = default_chain
        elif default_retriever:
            _default_chain = RetrievalQA.from_llm(
                llm, prompt=default_prompt, retriever=default_retriever
            )
        else:
            prompt_template = DEFAULT_TEMPLATE.replace("input", "query")
            prompt = PromptTemplate(
                template=prompt_template, input_variables=["history", "query"]
            )
            _default_chain = ConversationChain(
                llm=ChatOpenAI(), prompt=prompt, input_key="query", output_key="result"
            )
        return cls(
            router_chain=router_chain,
            destination_chains=destination_chains,
            default_chain=_default_chain,
            **kwargs,
        )
