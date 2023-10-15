"""Power BI agent."""
from typing import Any, Dict, List, Optional

from promptmanager.script.base.agents import AgentExecutor
from promptmanager.script.base.agents.agent import AgentOutputParser
from promptmanager.script.base.agents.agent_toolkits.powerbi.prompt import (
    POWERBI_CHAT_PREFIX,
    POWERBI_CHAT_SUFFIX,
)
from promptmanager.script.base.agents.agent_toolkits.powerbi.toolkit import PowerBIToolkit
from promptmanager.script.base.agents.conversational_chat.base import ConversationalChatAgent
from promptmanager.script.base.callbacks.base import BaseCallbackManager
from promptmanager.script.base.chat_models.base import BaseChatModel
from promptmanager.script.base.memory import ConversationBufferMemory
from promptmanager.script.base.memory.chat_memory import BaseChatMemory
from promptmanager.script.base.utilities.powerbi import PowerBIDataset


def create_pbi_chat_agent(
    llm: BaseChatModel,
    toolkit: Optional[PowerBIToolkit] = None,
    powerbi: Optional[PowerBIDataset] = None,
    callback_manager: Optional[BaseCallbackManager] = None,
    output_parser: Optional[AgentOutputParser] = None,
    prefix: str = POWERBI_CHAT_PREFIX,
    suffix: str = POWERBI_CHAT_SUFFIX,
    examples: Optional[str] = None,
    input_variables: Optional[List[str]] = None,
    memory: Optional[BaseChatMemory] = None,
    top_k: int = 10,
    verbose: bool = False,
    agent_executor_kwargs: Optional[Dict[str, Any]] = None,
    **kwargs: Dict[str, Any],
) -> AgentExecutor:
    """Construct a Power BI agent from a Chat LLM and tools.

    If you supply only a toolkit and no Power BI dataset, the same LLM is used for both.
    """
    if toolkit is None:
        if powerbi is None:
            raise ValueError("Must provide either a toolkit or powerbi dataset")
        toolkit = PowerBIToolkit(powerbi=powerbi, llm=llm, examples=examples)
    tools = toolkit.get_tools()
    tables = powerbi.table_names if powerbi else toolkit.powerbi.table_names
    agent = ConversationalChatAgent.from_llm_and_tools(
        llm=llm,
        tools=tools,
        system_message=prefix.format(top_k=top_k).format(tables=tables),
        human_message=suffix,
        input_variables=input_variables,
        callback_manager=callback_manager,
        output_parser=output_parser,
        verbose=verbose,
        **kwargs,
    )
    return AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=tools,
        callback_manager=callback_manager,
        memory=memory
        or ConversationBufferMemory(memory_key="chat_history", return_messages=True),
        verbose=verbose,
        **(agent_executor_kwargs or {}),
    )
