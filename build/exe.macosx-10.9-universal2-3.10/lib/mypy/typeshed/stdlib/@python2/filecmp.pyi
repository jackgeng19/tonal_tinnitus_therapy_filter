from typing import AnyStr, Callable, Generic, Iterable, Sequence, Text

DEFAULT_IGNORES: list[str]

def cmp(f1: bytes | Text, f2: bytes | Text, shallow: int | bool = ...) -> bool: ...
def cmpfiles(
    a: AnyStr, b: AnyStr, common: Iterable[AnyStr], shallow: int | bool = ...
) -> tuple[list[AnyStr], list[AnyStr], list[AnyStr]]: ...

class dircmp(Generic[AnyStr]):
    def __init__(
        self, a: AnyStr, b: AnyStr, ignore: Sequence[AnyStr] | None = ..., hide: Sequence[AnyStr] | None = ...
    ) -> None: ...
    left: AnyStr
    right: AnyStr
    hide: Sequence[AnyStr]
    ignore: Sequence[AnyStr]
    # These properties are created at runtime by __getattr__
    subdirs: dict[AnyStr, dircmp[AnyStr]]
    same_files: list[AnyStr]
    diff_files: list[AnyStr]
    funny_files: list[AnyStr]
    common_dirs: list[AnyStr]
    common_files: list[AnyStr]
    common_funny: list[AnyStr]
    common: list[AnyStr]
    left_only: list[AnyStr]
    right_only: list[AnyStr]
    left_list: list[AnyStr]
    right_list: list[AnyStr]
    def report(self) -> None: ...
    def report_partial_closure(self) -> None: ...
    def report_full_closure(self) -> None: ...
    methodmap: dict[str, Callable[[], None]]
    def phase0(self) -> None: ...
    def phase1(self) -> None: ...
    def phase2(self) -> None: ...
    def phase3(self) -> None: ...
    def phase4(self) -> None: ...
    def phase4_closure(self) -> None: ...