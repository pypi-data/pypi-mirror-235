from typing import List, Optional

import aiohttp
import requests

from promptmanager.script.base.callbacks.manager import (
    AsyncCallbackManagerForRetrieverRun,
    CallbackManagerForRetrieverRun,
)
from promptmanager.script.base.schema import BaseRetriever, Document


class RemotePMRetriever(BaseRetriever):
    """`Promptmanager API` retriever."""

    url: str
    """URL of the remote Promptmanager API."""
    headers: Optional[dict] = None
    """Headers to use for the request."""
    input_key: str = "message"
    """Key to use for the input in the request."""
    response_key: str = "response"
    """Key to use for the response in the request."""
    page_content_key: str = "page_content"
    """Key to use for the page content in the response."""
    metadata_key: str = "metadata"
    """Key to use for the metadata in the response."""

    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        response = requests.post(
            self.url, json={self.input_key: query}, headers=self.headers
        )
        result = response.json()
        return [
            Document(
                page_content=r[self.page_content_key], metadata=r[self.metadata_key]
            )
            for r in result[self.response_key]
        ]

    async def _aget_relevant_documents(
        self, query: str, *, run_manager: AsyncCallbackManagerForRetrieverRun
    ) -> List[Document]:
        async with aiohttp.ClientSession() as session:
            async with session.request(
                "POST", self.url, headers=self.headers, json={self.input_key: query}
            ) as response:
                result = await response.json()
        return [
            Document(
                page_content=r[self.page_content_key], metadata=r[self.metadata_key]
            )
            for r in result[self.response_key]
        ]
