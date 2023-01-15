import io
from _typeshed import ReadableBuffer, Self, WriteableBuffer
from typing import IO, Any, Iterable, Text
from typing_extensions import SupportsIndex

_PathOrFile = Text | IO[bytes]

def compress(data: bytes, compresslevel: int = ...) -> bytes: ...
def decompress(data: bytes) -> bytes: ...

class BZ2File(io.BufferedIOBase, IO[bytes]):
    def __enter__(self: Self) -> Self: ...
    def __init__(self, filename: _PathOrFile, mode: str = ..., buffering: Any | None = ..., compresslevel: int = ...) -> None: ...
    def read(self, size: int | None = ...) -> bytes: ...
    def read1(self, size: int = ...) -> bytes: ...
    def readline(self, size: SupportsIndex = ...) -> bytes: ...  # type: ignore[override]
    def readinto(self, b: WriteableBuffer) -> int: ...
    def readlines(self, size: SupportsIndex = ...) -> list[bytes]: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def write(self, data: ReadableBuffer) -> int: ...
    def writelines(self, seq: Iterable[ReadableBuffer]) -> None: ...

class BZ2Compressor(object):
    def __init__(self, compresslevel: int = ...) -> None: ...
    def compress(self, __data: bytes) -> bytes: ...
    def flush(self) -> bytes: ...

class BZ2Decompressor(object):
    def decompress(self, data: bytes) -> bytes: ...
    @property
    def unused_data(self) -> bytes: ...