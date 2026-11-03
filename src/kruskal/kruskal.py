from collections.abc import Hashable, Iterable, Sequence

from .merge_sort import merge_sort
from .union_find import UnionFind

Edge = tuple[Hashable, Hashable, float]


def kruskal(vertices: Iterable[Hashable], edges: Sequence[Edge]) -> list[Edge]:
    """Return a minimum spanning tree of an undirected graph.

    vertices lists the vertices. edges lists (u, v, weight) tuples. Edges are
    undirected, so (u, v, w) and (v, u, w) mean the same thing.

    Edges are taken in order of increasing weight. An edge joins the tree when its
    endpoints are in different components so far, which can never close a cycle.
    Among edges with equal weight, the one listed first wins.

    If the graph is disconnected, the result is a minimum spanning forest: one
    tree per connected component, V - C edges for C components.

    Raises ValueError if an edge uses a vertex that is not in vertices.
    """
    components = UnionFind(vertices)
    for u, v, _ in edges:
        for endpoint in (u, v):
            if endpoint not in components.parent:
                raise ValueError(f"edge ({u!r}, {v!r}) uses unknown vertex {endpoint!r}")

    max_edges = len(components.parent) - 1
    tree: list[Edge] = []
    for u, v, weight in merge_sort(edges, key=lambda edge: edge[2]):
        if len(tree) == max_edges:
            break
        if components.union(u, v):
            tree.append((u, v, weight))
    return tree
