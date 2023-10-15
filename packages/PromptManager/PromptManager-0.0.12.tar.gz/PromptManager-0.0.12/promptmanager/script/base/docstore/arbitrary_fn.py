from typing import Callable, Union

from promptmanager.script.base.docstore.base import Docstore
from promptmanager.script.base.schema import Document


class DocstoreFn(Docstore):
    """Promptmanager Docstore via arbitrary lookup function.

    This is useful when:
     * it's expensive to construct an InMemoryDocstore/dict
     * you retrieve documents from remote sources
     * you just want to reuse existing objects
    """

    def __init__(
        self,
        lookup_fn: Callable[[str], Union[Document, str]],
    ):
        self._lookup_fn = lookup_fn

    def search(self, search: str) -> Document:
        """Search for a document.

        Args:
            search: search string

        Returns:
            Document if found, else error message.
        """
        r = self._lookup_fn(search)
        if isinstance(r, str):
            # NOTE: assume the search string is the source ID
            return Document(page_content=r, metadata={"source": search})
        elif isinstance(r, Document):
            return r
        raise ValueError(f"Unexpected type of document {type(r)}")
