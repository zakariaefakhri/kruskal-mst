from collections.abc import Hashable, Iterable


class UnionFind:
    """Disjoint-set (union-find) structure over a fixed set of elements.

    find() uses path compression and union() attaches the smaller tree below the
    larger one. Together they make both operations run in amortized O(alpha(n))
    time, where alpha is the inverse Ackermann function (at most 4 in practice).
    """

    def __init__(self, elements: Iterable[Hashable]) -> None:
        # Every element starts as the root of its own set.
        self.parent = {v: v for v in elements}
        self.size = dict.fromkeys(self.parent, 1)

    def find(self, v: Hashable) -> Hashable:
        """Return the root of the set that contains v."""
        root = v
        while self.parent[root] != root:
            root = self.parent[root]
        # Path compression: point every node on the way directly at the root.
        while self.parent[v] != root:
            self.parent[v], v = root, self.parent[v]
        return root

    def union(self, v: Hashable, u: Hashable) -> bool:
        """Merge the sets of v and u. Return False if they were already one set."""
        v_root = self.find(v)
        u_root = self.find(u)
        if v_root == u_root:
            return False
        if self.size[v_root] < self.size[u_root]:
            v_root, u_root = u_root, v_root
        self.parent[u_root] = v_root
        self.size[v_root] += self.size[u_root]
        return True
