"""Requests toolkit."""
from __future__ import annotations

from typing import Any, List

from promptmanager.script.base.agents.agent import AgentExecutor
from promptmanager.script.base.agents.agent_toolkits.base import BaseToolkit
from promptmanager.script.base.agents.agent_toolkits.json.base import create_json_agent
from promptmanager.script.base.agents.agent_toolkits.json.toolkit import JsonToolkit
from promptmanager.script.base.agents.agent_toolkits.openapi.prompt import DESCRIPTION
from promptmanager.script.base.agents.tools import Tool
from promptmanager.script.base.schema.language_model import BaseLanguageModel
from promptmanager.script.base.tools import BaseTool
from promptmanager.script.base.tools.json.tool import JsonSpec
from promptmanager.script.base.tools.requests.tool import (
    RequestsDeleteTool,
    RequestsGetTool,
    RequestsPatchTool,
    RequestsPostTool,
    RequestsPutTool,
)
from promptmanager.script.base.utilities.requests import TextRequestsWrapper


class RequestsToolkit(BaseToolkit):
    """Toolkit for making REST requests."""

    requests_wrapper: TextRequestsWrapper

    def get_tools(self) -> List[BaseTool]:
        """Return a list of tools."""
        return [
            RequestsGetTool(requests_wrapper=self.requests_wrapper),
            RequestsPostTool(requests_wrapper=self.requests_wrapper),
            RequestsPatchTool(requests_wrapper=self.requests_wrapper),
            RequestsPutTool(requests_wrapper=self.requests_wrapper),
            RequestsDeleteTool(requests_wrapper=self.requests_wrapper),
        ]


class OpenAPIToolkit(BaseToolkit):
    """Toolkit for interacting with an OpenAPI API."""

    json_agent: AgentExecutor
    requests_wrapper: TextRequestsWrapper

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        json_agent_tool = Tool(
            name="json_explorer",
            func=self.json_agent.run,
            description=DESCRIPTION,
        )
        request_toolkit = RequestsToolkit(requests_wrapper=self.requests_wrapper)
        return [*request_toolkit.get_tools(), json_agent_tool]

    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        json_spec: JsonSpec,
        requests_wrapper: TextRequestsWrapper,
        **kwargs: Any,
    ) -> OpenAPIToolkit:
        """Create json agent from llm, then initialize."""
        json_agent = create_json_agent(llm, JsonToolkit(spec=json_spec), **kwargs)
        return cls(json_agent=json_agent, requests_wrapper=requests_wrapper)
