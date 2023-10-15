"""SQL agent."""
from typing import Any, Dict, List, Optional, Sequence

from promptmanager.script.base.agents.agent import AgentExecutor, BaseSingleActionAgent
from promptmanager.script.base.agents.agent_toolkits.sql.prompt import (
    SQL_FUNCTIONS_SUFFIX,
    SQL_PREFIX,
    SQL_SUFFIX,
)
from promptmanager.script.base.agents.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from promptmanager.script.base.agents.agent_types import AgentType
from promptmanager.script.base.agents.mrkl.base import ZeroShotAgent
from promptmanager.script.base.agents.mrkl.prompt import FORMAT_INSTRUCTIONS
from promptmanager.script.base.agents.openai_functions_agent.base import OpenAIFunctionsAgent
from promptmanager.script.base.callbacks.base import BaseCallbackManager
from promptmanager.script.base.chains.llm import LLMChain
from promptmanager.script.base.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from promptmanager.script.base.schema.language_model import BaseLanguageModel
from promptmanager.script.base.schema.messages import AIMessage, SystemMessage
from promptmanager.script.base.tools import BaseTool


def create_sql_agent(
    llm: BaseLanguageModel,
    toolkit: SQLDatabaseToolkit,
    agent_type: AgentType = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    callback_manager: Optional[BaseCallbackManager] = None,
    prefix: str = SQL_PREFIX,
    suffix: Optional[str] = None,
    format_instructions: str = FORMAT_INSTRUCTIONS,
    input_variables: Optional[List[str]] = None,
    top_k: int = 10,
    max_iterations: Optional[int] = 15,
    max_execution_time: Optional[float] = None,
    early_stopping_method: str = "force",
    verbose: bool = False,
    agent_executor_kwargs: Optional[Dict[str, Any]] = None,
    extra_tools: Sequence[BaseTool] = (),
    **kwargs: Dict[str, Any],
) -> AgentExecutor:
    """Construct an SQL agent from an LLM and tools."""
    tools = toolkit.get_tools() + list(extra_tools)
    prefix = prefix.format(dialect=toolkit.dialect, top_k=top_k)
    agent: BaseSingleActionAgent

    if agent_type == AgentType.ZERO_SHOT_REACT_DESCRIPTION:
        prompt = ZeroShotAgent.create_prompt(
            tools,
            prefix=prefix,
            suffix=suffix or SQL_SUFFIX,
            format_instructions=format_instructions,
            input_variables=input_variables,
        )
        llm_chain = LLMChain(
            llm=llm,
            prompt=prompt,
            callback_manager=callback_manager,
        )
        tool_names = [tool.name for tool in tools]
        agent = ZeroShotAgent(llm_chain=llm_chain, allowed_tools=tool_names, **kwargs)

    elif agent_type == AgentType.OPENAI_FUNCTIONS:
        messages = [
            SystemMessage(content=prefix),
            HumanMessagePromptTemplate.from_template("{input}"),
            AIMessage(content=suffix or SQL_FUNCTIONS_SUFFIX),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
        input_variables = ["input", "agent_scratchpad"]
        _prompt = ChatPromptTemplate(input_variables=input_variables, messages=messages)

        agent = OpenAIFunctionsAgent(
            llm=llm,
            prompt=_prompt,
            tools=tools,
            callback_manager=callback_manager,
            **kwargs,
        )
    else:
        raise ValueError(f"Agent type {agent_type} not supported at the moment.")

    return AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=tools,
        callback_manager=callback_manager,
        verbose=verbose,
        max_iterations=max_iterations,
        max_execution_time=max_execution_time,
        early_stopping_method=early_stopping_method,
        **(agent_executor_kwargs or {}),
    )
