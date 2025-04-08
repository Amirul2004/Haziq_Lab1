from types import NotImplementedType
from typing import Any, Literal
from typing_extensions import LiteralString, Self, Unpack

from sympy.polys.domains.domain import Domain
from sympy.polys.domains.domainelement import DomainElement
from sympy.polys.domains.field import Field
from sympy.polys.domains.integerring import ZZ
from sympy.polys.domains.rationalfield import QQ
from sympy.polys.domains.ring import Ring

class GaussianElement(DomainElement):  # type: ignore
    base: Domain
    _parent: Domain
    __slots__ = ...
    def __new__(cls, x, y=...): ...
    @classmethod
    def new(cls, x, y): ...
    def parent(self): ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __pos__(self) -> Self: ...
    def __neg__(self): ...
    def __repr__(self) -> LiteralString: ...
    def __add__(self, other) -> NotImplementedType: ...

    __radd__ = ...
    def __sub__(self, other) -> NotImplementedType: ...
    def __rsub__(self, other) -> NotImplementedType: ...
    def __mul__(self, other) -> NotImplementedType: ...

    __rmul__ = ...
    def __pow__(self, exp) -> float | Self: ...
    def __bool__(self) -> bool: ...
    def quadrant(self) -> Literal[0, 1, 2, 3]: ...
    def __rdivmod__(self, other) -> NotImplementedType: ...
    def __rtruediv__(self, other) -> NotImplementedType: ...
    def __floordiv__(self, other): ...
    def __rfloordiv__(self, other) -> NotImplementedType: ...
    def __mod__(self, other): ...
    def __rmod__(self, other) -> NotImplementedType: ...

class GaussianInteger(GaussianElement):
    base = ...
    def __truediv__(self, other): ...
    def __divmod__(self, other) -> NotImplementedType | tuple[GaussianInteger, Any]: ...

class GaussianRational(GaussianElement):
    base = ...
    def __truediv__(self, other) -> NotImplementedType | GaussianRational: ...
    def __divmod__(self, other) -> NotImplementedType | tuple[Any, Any]: ...

class GaussianDomain:
    dom: Domain = ...
    is_Numerical = ...
    is_Exact = ...
    has_assoc_Ring = ...
    has_assoc_Field = ...
    def to_sympy(self, a): ...
    def from_sympy(self, a): ...
    def inject(self, *gens): ...
    def canonical_unit(self, d): ...
    def is_negative(self, element) -> Literal[False]: ...
    def is_positive(self, element) -> Literal[False]: ...
    def is_nonnegative(self, element) -> Literal[False]: ...
    def is_nonpositive(self, element) -> Literal[False]: ...
    def from_ZZ_gmpy(K1, a, K0): ...
    def from_ZZ(K1, a, K0): ...
    def from_ZZ_python(K1, a, K0): ...
    def from_QQ(K1, a, K0): ...
    def from_QQ_gmpy(K1, a, K0): ...
    def from_QQ_python(K1, a, K0): ...
    def from_AlgebraicField(K1, a, K0) -> None: ...

class GaussianIntegerRing(GaussianDomain, Ring):
    dom = ...
    dtype = GaussianInteger
    zero = dtype(ZZ(0), ZZ(0))
    one = dtype(ZZ(1), ZZ(0))
    imag_unit = dtype(ZZ(0), ZZ(1))
    units = ...
    rep = ...
    is_GaussianRing = ...
    is_ZZ_I = ...
    def __init__(self) -> None: ...
    def get_ring(self) -> Self: ...
    def get_field(self) -> GaussianRationalField: ...
    def normalize(self, d, *args) -> tuple[Any, Unpack[tuple[Any, ...]]]: ...
    def gcd(self, a, b) -> tuple[Any, Unpack[tuple[Any, ...]]]: ...
    def lcm(self, a, b): ...
    def from_GaussianIntegerRing(K1, a, K0): ...
    def from_GaussianRationalField(K1, a, K0): ...

class GaussianRationalField(GaussianDomain, Field):
    dom = ...
    dtype = GaussianRational
    zero = dtype(QQ(0), QQ(0))
    one = dtype(QQ(1), QQ(0))
    imag_unit = dtype(QQ(0), QQ(1))
    units = ...
    rep = ...
    is_GaussianField = ...
    is_QQ_I = ...
    def __init__(self) -> None: ...
    def get_ring(self) -> GaussianIntegerRing: ...
    def get_field(self) -> Self: ...
    def as_AlgebraicField(self) -> Any: ...
    def numer(self, a): ...
    def denom(self, a): ...
    def from_GaussianIntegerRing(K1, a, K0): ...
    def from_GaussianRationalField(K1, a, K0): ...

QQ_I = ...
ZZ_I = ...
