import sys
from collections.abc import Iterable, Mapping
from typing import Any, Generic, TypeVar, overload
from typing_extensions import TypeAlias

if sys.version_info >= (3, 9):
    from types import GenericAlias

__all__ = ["CookieError", "BaseCookie", "SimpleCookie"]

_DataType: TypeAlias = str | Mapping[str, str | Morsel[Any]]
_T = TypeVar("_T")

@overload
def _quote(str: None) -> None: ...
@overload
def _quote(str: str) -> str: ...
@overload
def _unquote(str: None) -> None: ...
@overload
def _unquote(str: str) -> str: ...

class CookieError(Exception): ...

class Morsel(dict[str, Any], Generic[_T]):
    @property
    def value(self) -> str: ...
    @property
    def coded_value(self) -> _T: ...
    @property
    def key(self) -> str: ...
    def __init__(self) -> None: ...
    def set(self, key: str, val: str, coded_val: _T) -> None: ...
    def setdefault(self, key: str, val: str | None = None) -> str: ...
    # The dict update can also get a keywords argument so this is incompatible
    @overload  # type: ignore[override]
    def update(self, values: Mapping[str, str]) -> None: ...
    @overload
    def update(self, values: Iterable[tuple[str, str]]) -> None: ...
    def isReservedKey(self, K: str) -> bool: ...
    def output(self, attrs: list[str] | None = None, header: str = "Set-Cookie:") -> str: ...
    __str__ = output
    def js_output(self, attrs: list[str] | None = None) -> str: ...
    def OutputString(self, attrs: list[str] | None = None) -> str: ...
    def __eq__(self, morsel: object) -> bool: ...
    def __setitem__(self, K: str, V: Any) -> None: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

class BaseCookie(dict[str, Morsel[_T]], Generic[_T]):
    def __init__(self, input: _DataType | None = None) -> None: ...
    def value_decode(self, val: str) -> tuple[_T, str]: ...
    def value_encode(self, val: _T) -> tuple[_T, str]: ...
    def output(self, attrs: list[str] | None = None, header: str = "Set-Cookie:", sep: str = "\r\n") -> str: ...
    __str__ = output
    def js_output(self, attrs: list[str] | None = None) -> str: ...
    def load(self, rawdata: _DataType) -> None: ...
    def __setitem__(self, key: str, value: str | Morsel[_T]) -> None: ...

class SimpleCookie(BaseCookie[str]): ...
