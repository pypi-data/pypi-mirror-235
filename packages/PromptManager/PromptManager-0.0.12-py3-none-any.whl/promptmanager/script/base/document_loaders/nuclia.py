import json
import uuid
from typing import List

from promptmanager.script.base.docstore.document import Document
from promptmanager.script.base.document_loaders.base import BaseLoader
from promptmanager.script.base.tools.nuclia.tool import NucliaUnderstandingAPI


class NucliaLoader(BaseLoader):
    """Load from any file type using `Nuclia Understanding API`."""

    def __init__(self, path: str, nuclia_tool: NucliaUnderstandingAPI):
        self.nua = nuclia_tool
        self.id = str(uuid.uuid4())
        self.nua.run({"action": "push", "id": self.id, "path": path, "text": None})

    def load(self) -> List[Document]:
        """Load documents."""
        data = self.nua.run(
            {"action": "pull", "id": self.id, "path": None, "text": None}
        )
        if not data:
            return []
        obj = json.loads(data)
        text = obj["extracted_text"][0]["body"]["text"]
        print(text)
        metadata = {
            "file": obj["file_extracted_data"][0],
            "metadata": obj["field_metadata"][0],
        }
        return [Document(page_content=text, metadata=metadata)]
