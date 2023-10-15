from typing import List

from promptmanager.script.base.docstore.document import Document
from promptmanager.script.base.document_loaders.web_base import WebBaseLoader


class AZLyricsLoader(WebBaseLoader):
    """Load `AZLyrics` webpages."""

    def load(self) -> List[Document]:
        """Load webpages into Documents."""
        soup = self.scrape()
        title = soup.title.text
        lyrics = soup.find_all("div", {"class": ""})[2].text
        text = title + lyrics
        metadata = {"source": self.web_path}
        return [Document(page_content=text, metadata=metadata)]
