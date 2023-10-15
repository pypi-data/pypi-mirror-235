import os
import tempfile
from typing import Callable, List, Optional

from promptmanager.script.base.docstore.document import Document
from promptmanager.script.base.document_loaders.base import BaseLoader
from promptmanager.script.base.document_loaders.unstructured import UnstructuredFileLoader


class GCSFileLoader(BaseLoader):
    """Load from GCS file."""

    def __init__(
        self,
        project_name: str,
        bucket: str,
        blob: str,
        loader_func: Optional[Callable[[str], BaseLoader]] = None,
    ):
        """Initialize with bucket and key name.

        Args:
            project_name: The name of the project to load
            bucket: The name of the GCS bucket.
            blob: The name of the GCS blob to load.
            loader_func: A loader function that instantiates a loader based on a
                file_path argument. If nothing is provided, the
                UnstructuredFileLoader is used.

        Examples:
            To use an alternative PDF loader:
            >> from from promptmanager.script.base.document_loaders import PyPDFLoader
            >> loader = GCSFileLoader(..., loader_func=PyPDFLoader)

            To use UnstructuredFileLoader with additional arguments:
            >> loader = GCSFileLoader(...,
            >>      loader_func=lambda x: UnstructuredFileLoader(x, mode="elements"))

        """
        self.bucket = bucket
        self.blob = blob
        self.project_name = project_name

        def default_loader_func(file_path: str) -> BaseLoader:
            return UnstructuredFileLoader(file_path)

        self._loader_func = loader_func if loader_func else default_loader_func

    def load(self) -> List[Document]:
        """Load documents."""
        try:
            from google.cloud import storage
        except ImportError:
            raise ImportError(
                "Could not import google-cloud-storage python package. "
                "Please install it with `pip install google-cloud-storage`."
            )

        # Initialise a client
        storage_client = storage.Client(self.project_name)
        # Create a bucket object for our bucket
        bucket = storage_client.get_bucket(self.bucket)
        # Create a blob object from the filepath
        blob = bucket.blob(self.blob)
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = f"{temp_dir}/{self.blob}"
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            # Download the file to a destination
            blob.download_to_filename(file_path)
            loader = self._loader_func(file_path)
            docs = loader.load()
            for doc in docs:
                if "source" in doc.metadata:
                    doc.metadata["source"] = f"gs://{self.bucket}/{self.blob}"
            return docs
