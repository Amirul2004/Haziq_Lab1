from _typeshed import Unused
from collections.abc import Hashable

__all__ = ("hashkey", "methodkey", "typedkey", "typedmethodkey")

def hashkey(*args: Hashable, **kwargs: Hashable) -> tuple[Hashable, ...]: ...
def methodkey(self: Unused, *args: Hashable, **kwargs: Hashable) -> tuple[Hashable, ...]: ...
def typedkey(*args: Hashable, **kwargs: Hashable) -> tuple[Hashable, ...]: ...
def typedmethodkey(self: Unused, *args: Hashable, **kwargs: Hashable) -> tuple[Hashable, ...]: ...
