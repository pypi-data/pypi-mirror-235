from __future__ import annotations

from typing import List, Optional

from promptmanager.script.base.agents.agent_toolkits.base import BaseToolkit
from promptmanager.script.base.pydantic_v1 import root_validator
from promptmanager.script.base.tools import BaseTool
from promptmanager.script.base.tools.file_management.copy import CopyFileTool
from promptmanager.script.base.tools.file_management.delete import DeleteFileTool
from promptmanager.script.base.tools.file_management.file_search import FileSearchTool
from promptmanager.script.base.tools.file_management.list_dir import ListDirectoryTool
from promptmanager.script.base.tools.file_management.move import MoveFileTool
from promptmanager.script.base.tools.file_management.read import ReadFileTool
from promptmanager.script.base.tools.file_management.write import WriteFileTool

_FILE_TOOLS = {
    # "Type[Runnable[Any, Any]]" has no attribute "__fields__"  [attr-defined]
    tool_cls.__fields__["name"].default: tool_cls  # type: ignore[attr-defined]
    for tool_cls in [
        CopyFileTool,
        DeleteFileTool,
        FileSearchTool,
        MoveFileTool,
        ReadFileTool,
        WriteFileTool,
        ListDirectoryTool,
    ]
}


class FileManagementToolkit(BaseToolkit):
    """Toolkit for interacting with a Local Files."""

    root_dir: Optional[str] = None
    """If specified, all file operations are made relative to root_dir."""
    selected_tools: Optional[List[str]] = None
    """If provided, only provide the selected tools. Defaults to all."""

    @root_validator
    def validate_tools(cls, values: dict) -> dict:
        selected_tools = values.get("selected_tools") or []
        for tool_name in selected_tools:
            if tool_name not in _FILE_TOOLS:
                raise ValueError(
                    f"File Tool of name {tool_name} not supported."
                    f" Permitted tools: {list(_FILE_TOOLS)}"
                )
        return values

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        allowed_tools = self.selected_tools or _FILE_TOOLS.keys()
        tools: List[BaseTool] = []
        for tool in allowed_tools:
            tool_cls = _FILE_TOOLS[tool]
            tools.append(tool_cls(root_dir=self.root_dir))  # type: ignore
        return tools


__all__ = ["FileManagementToolkit"]
