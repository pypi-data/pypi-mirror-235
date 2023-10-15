import json
import logging
from pathlib import Path
from typing import Iterator, Union

from promptmanager.script.base.chat_loaders.base import BaseChatLoader
from promptmanager.script.base.schema.chat import ChatSession
from promptmanager.script.base.schema.messages import HumanMessage

logger = logging.getLogger(__file__)


class SingleFileFacebookMessengerChatLoader(BaseChatLoader):
    """Load `Facebook Messenger` chat data from a single file.

    Args:
        path (Union[Path, str]): The path to the chat file.

    Attributes:
        path (Path): The path to the chat file.

    """

    def __init__(self, path: Union[Path, str]) -> None:
        super().__init__()
        self.file_path = path if isinstance(path, Path) else Path(path)

    def lazy_load(self) -> Iterator[ChatSession]:
        """Lazy loads the chat data from the file.

        Yields:
            ChatSession: A chat session containing the loaded messages.

        """
        with open(self.file_path) as f:
            data = json.load(f)
        sorted_data = sorted(data["messages"], key=lambda x: x["timestamp_ms"])
        messages = []
        for m in sorted_data:
            messages.append(
                HumanMessage(
                    content=m["content"], additional_kwargs={"sender": m["sender_name"]}
                )
            )
        yield ChatSession(messages=messages)


class FolderFacebookMessengerChatLoader(BaseChatLoader):
    """Load `Facebook Messenger` chat data from a folder.

    Args:
        path (Union[str, Path]): The path to the directory
            containing the chat files.

    Attributes:
        path (Path): The path to the directory containing the chat files.

    """

    def __init__(self, path: Union[str, Path]) -> None:
        super().__init__()
        self.directory_path = Path(path) if isinstance(path, str) else path

    def lazy_load(self) -> Iterator[ChatSession]:
        """Lazy loads the chat data from the folder.

        Yields:
            ChatSession: A chat session containing the loaded messages.

        """
        inbox_path = self.directory_path / "inbox"
        for _dir in inbox_path.iterdir():
            if _dir.is_dir():
                for _file in _dir.iterdir():
                    if _file.suffix.lower() == ".json":
                        file_loader = SingleFileFacebookMessengerChatLoader(path=_file)
                        for result in file_loader.lazy_load():
                            yield result
