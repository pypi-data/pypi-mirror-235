from typing import Any, List, Optional

from promptmanager.script.base.agents.agent import AgentExecutor
from promptmanager.script.base.agents.openai_functions_agent.agent_token_buffer_memory import (
    AgentTokenBufferMemory,
)
from promptmanager.script.base.agents.openai_functions_agent.base import OpenAIFunctionsAgent
from promptmanager.script.base.chat_models.openai import ChatOpenAI
from promptmanager.script.base.memory.token_buffer import ConversationTokenBufferMemory
from promptmanager.script.base.prompts.chat import MessagesPlaceholder
from promptmanager.script.base.schema.language_model import BaseLanguageModel
from promptmanager.script.base.schema.memory import BaseMemory
from promptmanager.script.base.schema.messages import SystemMessage
from promptmanager.script.base.tools.base import BaseTool


def _get_default_system_message() -> SystemMessage:
    return SystemMessage(
        content=(
            "Do your best to answer the questions. "
            "Feel free to use any tools available to look up "
            "relevant information, only if necessary"
        )
    )


def create_conversational_retrieval_agent(
    llm: BaseLanguageModel,
    tools: List[BaseTool],
    remember_intermediate_steps: bool = True,
    memory_key: str = "chat_history",
    system_message: Optional[SystemMessage] = None,
    verbose: bool = False,
    max_token_limit: int = 2000,
    **kwargs: Any
) -> AgentExecutor:
    """A convenience method for creating a conversational retrieval agent.

    Args:
        llm: The language model to use, should be ChatOpenAI
        tools: A list of tools the agent has access to
        remember_intermediate_steps: Whether the agent should remember intermediate
            steps or not. Intermediate steps refer to prior action/observation
            pairs from previous questions. The benefit of remembering these is if
            there is relevant information in there, the agent can use it to answer
            follow up questions. The downside is it will take up more tokens.
        memory_key: The name of the memory key in the prompt.
        system_message: The system message to use. By default, a basic one will
            be used.
        verbose: Whether or not the final AgentExecutor should be verbose or not,
            defaults to False.
        max_token_limit: The max number of tokens to keep around in memory.
            Defaults to 2000.

    Returns:
        An agent executor initialized appropriately
    """

    if not isinstance(llm, ChatOpenAI):
        raise ValueError("Only supported with ChatOpenAI models.")
    if remember_intermediate_steps:
        memory: BaseMemory = AgentTokenBufferMemory(
            memory_key=memory_key, llm=llm, max_token_limit=max_token_limit
        )
    else:
        memory = ConversationTokenBufferMemory(
            memory_key=memory_key,
            return_messages=True,
            output_key="output",
            llm=llm,
            max_token_limit=max_token_limit,
        )

    _system_message = system_message or _get_default_system_message()
    prompt = OpenAIFunctionsAgent.create_prompt(
        system_message=_system_message,
        extra_prompt_messages=[MessagesPlaceholder(variable_name=memory_key)],
    )
    agent = OpenAIFunctionsAgent(llm=llm, tools=tools, prompt=prompt)
    return AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=verbose,
        return_intermediate_steps=remember_intermediate_steps,
        **kwargs
    )
