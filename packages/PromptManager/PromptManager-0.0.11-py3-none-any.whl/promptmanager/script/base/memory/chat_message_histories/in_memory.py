from typing import List

from promptmanager.script.base.pydantic_v1 import BaseModel, Field
from promptmanager.script.base.schema import (
    BaseChatMessageHistory,
)
from promptmanager.script.base.schema.messages import BaseMessage


class ChatMessageHistory(BaseChatMessageHistory, BaseModel):
    """In memory implementation of chat message history.

    Stores messages in an in memory list.
    """

    messages: List[BaseMessage] = Field(default_factory=list)

    def add_message(self, message: BaseMessage) -> None:
        """Add a self-created message to the store"""
        self.messages.append(message)

    def clear(self) -> None:
        self.messages = []
