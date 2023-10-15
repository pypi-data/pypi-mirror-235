"""GitHub Toolkit."""
from typing import Dict, List

from promptmanager.script.base.agents.agent_toolkits.base import BaseToolkit
from promptmanager.script.base.tools import BaseTool
from promptmanager.script.base.tools.gitlab.prompt import (
    COMMENT_ON_ISSUE_PROMPT,
    CREATE_FILE_PROMPT,
    CREATE_PULL_REQUEST_PROMPT,
    DELETE_FILE_PROMPT,
    GET_ISSUE_PROMPT,
    GET_ISSUES_PROMPT,
    READ_FILE_PROMPT,
    UPDATE_FILE_PROMPT,
)
from promptmanager.script.base.tools.gitlab.tool import GitLabAction
from promptmanager.script.base.utilities.gitlab import GitLabAPIWrapper


class GitLabToolkit(BaseToolkit):
    """GitLab Toolkit."""

    tools: List[BaseTool] = []

    @classmethod
    def from_gitlab_api_wrapper(
        cls, gitlab_api_wrapper: GitLabAPIWrapper
    ) -> "GitLabToolkit":
        operations: List[Dict] = [
            {
                "mode": "get_issues",
                "name": "Get Issues",
                "description": GET_ISSUES_PROMPT,
            },
            {
                "mode": "get_issue",
                "name": "Get Issue",
                "description": GET_ISSUE_PROMPT,
            },
            {
                "mode": "comment_on_issue",
                "name": "Comment on Issue",
                "description": COMMENT_ON_ISSUE_PROMPT,
            },
            {
                "mode": "create_pull_request",
                "name": "Create Pull Request",
                "description": CREATE_PULL_REQUEST_PROMPT,
            },
            {
                "mode": "create_file",
                "name": "Create File",
                "description": CREATE_FILE_PROMPT,
            },
            {
                "mode": "read_file",
                "name": "Read File",
                "description": READ_FILE_PROMPT,
            },
            {
                "mode": "update_file",
                "name": "Update File",
                "description": UPDATE_FILE_PROMPT,
            },
            {
                "mode": "delete_file",
                "name": "Delete File",
                "description": DELETE_FILE_PROMPT,
            },
        ]
        tools = [
            GitLabAction(
                name=action["name"],
                description=action["description"],
                mode=action["mode"],
                api_wrapper=gitlab_api_wrapper,
            )
            for action in operations
        ]
        return cls(tools=tools)

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return self.tools
