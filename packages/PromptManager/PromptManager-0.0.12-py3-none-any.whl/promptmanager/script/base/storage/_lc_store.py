"""Create a key-value store for any promptmanager serializable object."""
from typing import Callable, Optional

from promptmanager.script.base.load.dump import dumps
from promptmanager.script.base.load.load import loads
from promptmanager.script.base.load.serializable import Serializable
from promptmanager.script.base.schema import BaseStore, Document
from promptmanager.script.base.storage.encoder_backed import EncoderBackedStore


def _dump_as_bytes(obj: Serializable) -> bytes:
    """Return a bytes representation of a document."""
    return dumps(obj).encode("utf-8")


def _dump_document_as_bytes(obj: Document) -> bytes:
    """Return a bytes representation of a document."""
    if not isinstance(obj, Document):
        raise TypeError("Expected a Document instance")
    return dumps(obj).encode("utf-8")


def _load_document_from_bytes(serialized: bytes) -> Document:
    """Return a document from a bytes representation."""
    obj = loads(serialized.decode("utf-8"))
    if not isinstance(obj, Document):
        raise TypeError(f"Expected a Document instance. Got {type(obj)}")
    return obj


def _load_from_bytes(serialized: bytes) -> Serializable:
    """Return a document from a bytes representation."""
    return loads(serialized.decode("utf-8"))


def _identity(x: str) -> str:
    """Return the same object."""
    return x


# PUBLIC API


def create_lc_store(
    store: BaseStore[str, bytes],
    *,
    key_encoder: Optional[Callable[[str], str]] = None,
) -> BaseStore[str, Serializable]:
    """Create a store for promptmanager serializable objects from a bytes store.

    Args:
        store: A bytes store to use as the underlying store.
        key_encoder: A function to encode keys; if None uses identity function.

    Returns:
        A key-value store for documents.
    """
    return EncoderBackedStore(
        store,
        key_encoder or _identity,
        _dump_as_bytes,
        _load_from_bytes,
    )


def create_kv_docstore(
    store: BaseStore[str, bytes],
    *,
    key_encoder: Optional[Callable[[str], str]] = None,
) -> BaseStore[str, Document]:
    """Create a store for promptmanager Document objects from a bytes store.

    This store does run time type checking to ensure that the values are
    Document objects.

    Args:
        store: A bytes store to use as the underlying store.
        key_encoder: A function to encode keys; if None uses identity function.

    Returns:
        A key-value store for documents.
    """
    return EncoderBackedStore(
        store,
        key_encoder or _identity,
        _dump_document_as_bytes,
        _load_document_from_bytes,
    )
