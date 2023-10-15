from __future__ import annotations

import logging
from abc import abstractmethod
from typing import Any, Dict, List, Optional

import requests

from promptmanager.script.base.callbacks.manager import CallbackManagerForToolRun
from promptmanager.script.base.pydantic_v1 import root_validator
from promptmanager.script.base.tools.base import BaseTool
from promptmanager.script.base.utils import get_from_dict_or_env

logger = logging.getLogger(__name__)


class EdenaiTool(BaseTool):

    """
    the base tool for all the EdenAI Tools .
    you should have
    the environment variable ``EDENAI_API_KEY`` set with your API token.
    You can find your token here: https://app.edenai.run/admin/account/settings
    """

    feature: str
    subfeature: str
    edenai_api_key: Optional[str] = None
    is_async: bool = False

    providers: List[str]
    """provider to use for the API call."""

    @root_validator(allow_reuse=True)
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key exists in environment."""
        values["edenai_api_key"] = get_from_dict_or_env(
            values, "edenai_api_key", "EDENAI_API_KEY"
        )
        return values

    @staticmethod
    def get_user_agent() -> str:
        from promptmanager.script.base import __version__

        return f"promptmanager/{__version__}"

    def _call_eden_ai(self, query_params: Dict[str, Any]) -> str:
        """
        Make an API call to the EdenAI service with the specified query parameters.

        Args:
            query_params (dict): The parameters to include in the API call.

        Returns:
            requests.Response: The response from the EdenAI API call.

        """

        # faire l'API call

        headers = {
            "Authorization": f"Bearer {self.edenai_api_key}",
            "User-Agent": self.get_user_agent(),
        }

        url = f"https://api.edenai.run/v2/{self.feature}/{self.subfeature}"

        payload = {
            "providers": str(self.providers),
            "response_as_dict": False,
            "attributes_as_list": True,
            "show_original_response": False,
        }

        payload.update(query_params)

        response = requests.post(url, json=payload, headers=headers)

        self._raise_on_error(response)

        try:
            return self._parse_response(response.json())
        except Exception as e:
            raise RuntimeError(f"An error occurred while running tool: {e}")

    def _raise_on_error(self, response: requests.Response) -> None:
        if response.status_code >= 500:
            raise Exception(f"EdenAI Server: Error {response.status_code}")
        elif response.status_code >= 400:
            raise ValueError(f"EdenAI received an invalid payload: {response.text}")
        elif response.status_code != 200:
            raise Exception(
                f"EdenAI returned an unexpected response with status "
                f"{response.status_code}: {response.text}"
            )

        # case where edenai call succeeded but provider returned an error
        # (eg: rate limit, server error, etc.)
        if self.is_async is False:
            # async call are different and only return a job_id,
            # not the provider response directly
            provider_response = response.json()[0]
            if provider_response.get("status") == "fail":
                err_msg = provider_response["error"]["message"]
                raise ValueError(err_msg)

    @abstractmethod
    def _run(
        self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        pass

    @abstractmethod
    def _parse_response(self, response: Any) -> str:
        """Take a dict response and condense it's data in a human readable string"""
        pass

    def _get_edenai(self, url: str) -> requests.Response:
        headers = {
            "accept": "application/json",
            "authorization": f"Bearer {self.edenai_api_key}",
            "User-Agent": self.get_user_agent(),
        }

        response = requests.get(url, headers=headers)

        self._raise_on_error(response)

        return response

    def _parse_json_multilevel(
        self, extracted_data: dict, formatted_list: list, level: int = 0
    ) -> None:
        for section, subsections in extracted_data.items():
            indentation = "  " * level
            if isinstance(subsections, str):
                subsections = subsections.replace("\n", ",")
                formatted_list.append(f"{indentation}{section} : {subsections}")

            elif isinstance(subsections, list):
                formatted_list.append(f"{indentation}{section} : ")
                self._list_handling(subsections, formatted_list, level + 1)

            elif isinstance(subsections, dict):
                formatted_list.append(f"{indentation}{section} : ")
                self._parse_json_multilevel(subsections, formatted_list, level + 1)

    def _list_handling(
        self, subsection_list: list, formatted_list: list, level: int
    ) -> None:
        for list_item in subsection_list:
            if isinstance(list_item, dict):
                self._parse_json_multilevel(list_item, formatted_list, level)

            elif isinstance(list_item, list):
                self._list_handling(list_item, formatted_list, level + 1)

            else:
                formatted_list.append(f"{'  ' * level}{list_item}")
