"""Parsing utils to go from string to AgentAction or Agent Finish.

AgentAction means that an action should be taken.
This contains the name of the tool to use, the input to pass to that tool,
and a `log` variable (which contains a log of the agent's thinking).

AgentFinish means that a response should be given.
This contains a `return_values` dictionary. This usually contains a
single `output` key, but can be extended to contain more.
This also contains a `log` variable (which contains a log of the agent's thinking).
"""
from promptmanager.script.base.agents.output_parsers.json import JSONAgentOutputParser
from promptmanager.script.base.agents.output_parsers.openai_functions import (
    OpenAIFunctionsAgentOutputParser,
)
from promptmanager.script.base.agents.output_parsers.react_json_single_input import (
    ReActJsonSingleInputOutputParser,
)
from promptmanager.script.base.agents.output_parsers.react_single_input import (
    ReActSingleInputOutputParser,
)
from promptmanager.script.base.agents.output_parsers.self_ask import SelfAskOutputParser
from promptmanager.script.base.agents.output_parsers.xml import XMLAgentOutputParser

__all__ = [
    "ReActSingleInputOutputParser",
    "SelfAskOutputParser",
    "ReActJsonSingleInputOutputParser",
    "OpenAIFunctionsAgentOutputParser",
    "XMLAgentOutputParser",
    "JSONAgentOutputParser",
]
