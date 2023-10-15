from typing import Dict, List

from promptmanager.script.base.agents.agent_toolkits.base import BaseToolkit
from promptmanager.script.base.tools import BaseTool
from promptmanager.script.base.tools.clickup.prompt import (
    CLICKUP_FOLDER_CREATE_PROMPT,
    CLICKUP_GET_ALL_TEAMS_PROMPT,
    CLICKUP_GET_FOLDERS_PROMPT,
    CLICKUP_GET_LIST_PROMPT,
    CLICKUP_GET_SPACES_PROMPT,
    CLICKUP_GET_TASK_ATTRIBUTE_PROMPT,
    CLICKUP_GET_TASK_PROMPT,
    CLICKUP_LIST_CREATE_PROMPT,
    CLICKUP_TASK_CREATE_PROMPT,
    CLICKUP_UPDATE_TASK_ASSIGNEE_PROMPT,
    CLICKUP_UPDATE_TASK_PROMPT,
)
from promptmanager.script.base.tools.clickup.tool import ClickupAction
from promptmanager.script.base.utilities.clickup import ClickupAPIWrapper


class ClickupToolkit(BaseToolkit):
    """Clickup Toolkit."""

    tools: List[BaseTool] = []

    @classmethod
    def from_clickup_api_wrapper(
        cls, clickup_api_wrapper: ClickupAPIWrapper
    ) -> "ClickupToolkit":
        operations: List[Dict] = [
            {
                "mode": "get_task",
                "name": "Get task",
                "description": CLICKUP_GET_TASK_PROMPT,
            },
            {
                "mode": "get_task_attribute",
                "name": "Get task attribute",
                "description": CLICKUP_GET_TASK_ATTRIBUTE_PROMPT,
            },
            {
                "mode": "get_teams",
                "name": "Get Teams",
                "description": CLICKUP_GET_ALL_TEAMS_PROMPT,
            },
            {
                "mode": "create_task",
                "name": "Create Task",
                "description": CLICKUP_TASK_CREATE_PROMPT,
            },
            {
                "mode": "create_list",
                "name": "Create List",
                "description": CLICKUP_LIST_CREATE_PROMPT,
            },
            {
                "mode": "create_folder",
                "name": "Create Folder",
                "description": CLICKUP_FOLDER_CREATE_PROMPT,
            },
            {
                "mode": "get_list",
                "name": "Get all lists in the space",
                "description": CLICKUP_GET_LIST_PROMPT,
            },
            {
                "mode": "get_folders",
                "name": "Get all folders in the workspace",
                "description": CLICKUP_GET_FOLDERS_PROMPT,
            },
            {
                "mode": "get_spaces",
                "name": "Get all spaces in the workspace",
                "description": CLICKUP_GET_SPACES_PROMPT,
            },
            {
                "mode": "update_task",
                "name": "Update task",
                "description": CLICKUP_UPDATE_TASK_PROMPT,
            },
            {
                "mode": "update_task_assignees",
                "name": "Update task assignees",
                "description": CLICKUP_UPDATE_TASK_ASSIGNEE_PROMPT,
            },
        ]
        tools = [
            ClickupAction(
                name=action["name"],
                description=action["description"],
                mode=action["mode"],
                api_wrapper=clickup_api_wrapper,
            )
            for action in operations
        ]
        return cls(tools=tools)

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return self.tools
