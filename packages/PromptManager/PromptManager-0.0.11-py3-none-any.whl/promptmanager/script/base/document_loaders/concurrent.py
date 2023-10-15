from __future__ import annotations

import concurrent.futures
from pathlib import Path
from typing import Iterator, Literal, Optional, Sequence, Union

from promptmanager.script.base.document_loaders.base import BaseBlobParser
from promptmanager.script.base.document_loaders.blob_loaders import BlobLoader, FileSystemBlobLoader
from promptmanager.script.base.document_loaders.generic import GenericLoader
from promptmanager.script.base.document_loaders.parsers.registry import get_parser
from promptmanager.script.base.schema import Document

_PathLike = Union[str, Path]

DEFAULT = Literal["default"]


class ConcurrentLoader(GenericLoader):
    """Load and pars Documents concurrently."""

    def __init__(
        self, blob_loader: BlobLoader, blob_parser: BaseBlobParser, num_workers: int = 4
    ) -> None:
        super().__init__(blob_loader, blob_parser)
        self.num_workers = num_workers

    def lazy_load(
        self,
    ) -> Iterator[Document]:
        """Load documents lazily with concurrent parsing."""
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.num_workers
        ) as executor:
            futures = {
                executor.submit(self.blob_parser.lazy_parse, blob)
                for blob in self.blob_loader.yield_blobs()
            }
            for future in concurrent.futures.as_completed(futures):
                yield from future.result()

    @classmethod
    def from_filesystem(
        cls,
        path: _PathLike,
        *,
        glob: str = "**/[!.]*",
        exclude: Sequence[str] = (),
        suffixes: Optional[Sequence[str]] = None,
        show_progress: bool = False,
        parser: Union[DEFAULT, BaseBlobParser] = "default",
        num_workers: int = 4,
    ) -> ConcurrentLoader:
        """
        Create a concurrent generic document loader using a
        filesystem blob loader.


        Args:
            path: The path to the directory to load documents from.
            glob: The glob pattern to use to find documents.
            suffixes: The suffixes to use to filter documents. If None, all files
                      matching the glob will be loaded.
            exclude: A list of patterns to exclude from the loader.
            show_progress: Whether to show a progress bar or not (requires tqdm).
                           Proxies to the file system loader.
            parser: A blob parser which knows how to parse blobs into documents
            num_workers: Max number of concurrent workers to use.
        """
        blob_loader = FileSystemBlobLoader(
            path,
            glob=glob,
            exclude=exclude,
            suffixes=suffixes,
            show_progress=show_progress,
        )
        if isinstance(parser, str):
            blob_parser = get_parser(parser)
        else:
            blob_parser = parser
        return cls(blob_loader, blob_parser, num_workers=num_workers)
