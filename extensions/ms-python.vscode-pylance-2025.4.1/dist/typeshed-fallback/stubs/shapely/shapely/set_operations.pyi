from typing import overload

from ._typing import GeoArray, OptGeoArrayLike, OptGeoArrayLikeSeq
from .geometry.base import BaseGeometry
from .lib import Geometry

__all__ = [
    "difference",
    "intersection",
    "intersection_all",
    "symmetric_difference",
    "symmetric_difference_all",
    "unary_union",
    "union",
    "union_all",
    "coverage_union",
    "coverage_union_all",
]

@overload
def difference(a: Geometry, b: Geometry, grid_size: float | None = None, **kwargs) -> BaseGeometry: ...
@overload
def difference(a: None, b: Geometry | None, grid_size: float | None = None, **kwargs) -> None: ...
@overload
def difference(a: Geometry | None, b: None, grid_size: float | None = None, **kwargs) -> None: ...
@overload
def difference(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, grid_size: float | None = None, **kwargs) -> GeoArray: ...
@overload
def difference(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, grid_size: float | None = None, **kwargs) -> GeoArray: ...
@overload
def intersection(a: Geometry, b: Geometry, grid_size: float | None = None, **kwargs) -> BaseGeometry: ...
@overload
def intersection(a: None, b: Geometry | None, grid_size: float | None = None, **kwargs) -> None: ...
@overload
def intersection(a: Geometry | None, b: None, grid_size: float | None = None, **kwargs) -> None: ...
@overload
def intersection(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, grid_size: float | None = None, **kwargs) -> GeoArray: ...
@overload
def intersection(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, grid_size: float | None = None, **kwargs) -> GeoArray: ...
@overload
def intersection_all(geometries: OptGeoArrayLike, axis: None = None, **kwargs) -> BaseGeometry: ...
@overload
def intersection_all(geometries: OptGeoArrayLikeSeq, axis: int, **kwargs) -> BaseGeometry | GeoArray: ...
@overload
def symmetric_difference(a: Geometry, b: Geometry, grid_size: float | None = None, **kwargs) -> BaseGeometry: ...
@overload
def symmetric_difference(a: None, b: Geometry | None, grid_size: float | None = None, **kwargs) -> None: ...
@overload
def symmetric_difference(a: Geometry | None, b: None, grid_size: float | None = None, **kwargs) -> None: ...
@overload
def symmetric_difference(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, grid_size: float | None = None, **kwargs) -> GeoArray: ...
@overload
def symmetric_difference(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, grid_size: float | None = None, **kwargs) -> GeoArray: ...
@overload
def symmetric_difference_all(geometries: OptGeoArrayLike, axis: None = None, **kwargs) -> BaseGeometry: ...
@overload
def symmetric_difference_all(geometries: OptGeoArrayLikeSeq, axis: int, **kwargs) -> BaseGeometry | GeoArray: ...
@overload
def union(a: Geometry, b: Geometry, grid_size: float | None = None, **kwargs) -> BaseGeometry: ...
@overload
def union(a: None, b: Geometry | None, grid_size: float | None = None, **kwargs) -> None: ...
@overload
def union(a: Geometry | None, b: None, grid_size: float | None = None, **kwargs) -> None: ...
@overload
def union(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, grid_size: float | None = None, **kwargs) -> GeoArray: ...
@overload
def union(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, grid_size: float | None = None, **kwargs) -> GeoArray: ...
@overload
def union_all(geometries: OptGeoArrayLike, grid_size: float | None = None, axis: None = None, **kwargs) -> BaseGeometry: ...
@overload
def union_all(
    geometries: OptGeoArrayLikeSeq, grid_size: float | None = None, *, axis: int, **kwargs
) -> BaseGeometry | GeoArray: ...
@overload
def union_all(geometries: OptGeoArrayLikeSeq, grid_size: float | None, axis: int, **kwargs) -> BaseGeometry | GeoArray: ...

unary_union = union_all

@overload
def coverage_union(a: OptGeoArrayLike, b: OptGeoArrayLike, *, axis: None = None, **kwargs) -> BaseGeometry: ...
@overload
def coverage_union(a: OptGeoArrayLike, b: OptGeoArrayLike, *, axis: int, **kwargs) -> BaseGeometry | GeoArray: ...
@overload
def coverage_union_all(geometries: OptGeoArrayLike, axis: None = None, **kwargs) -> BaseGeometry: ...
@overload
def coverage_union_all(geometries: OptGeoArrayLikeSeq, axis: int, **kwargs) -> BaseGeometry | GeoArray: ...
