from _typeshed import Incomplete, SupportsGetItem

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def global_reaching_centrality(G: DiGraph[_Node], weight: str | None = None, normalized: bool | None = True): ...
@_dispatchable
def local_reaching_centrality(
    G: DiGraph[_Node],
    v: _Node,
    paths: SupportsGetItem[Incomplete, Incomplete] | None = None,
    weight: str | None = None,
    normalized: bool | None = True,
): ...
