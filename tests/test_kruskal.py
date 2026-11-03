import itertools
import random

import pytest

from kruskal import kruskal

VERTICES = ["A", "B", "C", "D", "E"]
EDGES = [
    ("A", "B", 2),
    ("A", "D", 3),
    ("A", "C", 1),
    ("A", "E", 2),
    ("B", "C", 3),
    ("C", "D", 8),
    ("D", "E", 5),
    ("C", "E", 1),
]


def total(edges):
    return sum(w for _, _, w in edges)


def test_hand_checked_graph():
    assert kruskal(VERTICES, EDGES) == [("A", "C", 1), ("C", "E", 1), ("A", "B", 2), ("A", "D", 3)]


def test_input_is_not_modified():
    edges = list(EDGES)
    kruskal(VERTICES, edges)
    assert edges == EDGES


def test_empty_graph_and_single_vertex():
    assert kruskal([], []) == []
    assert kruskal(["A"], []) == []


def test_disconnected_graph_gives_spanning_forest():
    tree = kruskal([*VERTICES, "X", "Y", "Z"], [*EDGES, ("X", "Y", 4)])
    assert ("X", "Y", 4) in tree
    assert len(tree) == 5  # 8 vertices, 3 components
    assert total(tree) == 11


def test_self_loops_and_parallel_edges():
    edges = [("A", "A", 0), ("A", "B", 5), ("A", "B", 1), ("B", "A", 3)]
    assert kruskal(["A", "B"], edges) == [("A", "B", 1)]


def test_equal_weights_keep_input_order():
    edges = [("A", "B", 1), ("B", "C", 1), ("A", "C", 1)]
    assert kruskal(["A", "B", "C"], edges) == [("A", "B", 1), ("B", "C", 1)]


def test_negative_and_float_weights():
    edges = [("A", "B", -2.5), ("B", "C", 0.5), ("A", "C", -1.0)]
    assert kruskal(["A", "B", "C"], edges) == [("A", "B", -2.5), ("A", "C", -1.0)]


def test_unknown_vertex_raises():
    with pytest.raises(ValueError, match="unknown vertex"):
        kruskal(["A", "B"], [("A", "C", 1)])


def test_long_path_graph():
    n = 5000
    edges = [(i + 1, i, i) for i in range(n - 1)] + [(0, n - 1, n)]
    tree = kruskal(range(n), edges)
    assert len(tree) == n - 1
    assert (0, n - 1, n) not in tree


def is_forest(vertices, edges):
    parent = {v: v for v in vertices}

    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v

    for u, v, _ in edges:
        ru, rv = root(u), root(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return True


def component_count(vertices, edges):
    seen, count = set(), 0
    adjacent = {v: set() for v in vertices}
    for u, v, _ in edges:
        adjacent[u].add(v)
        adjacent[v].add(u)
    for start in vertices:
        if start in seen:
            continue
        count += 1
        stack = [start]
        while stack:
            v = stack.pop()
            if v not in seen:
                seen.add(v)
                stack.extend(adjacent[v])
    return count


def brute_force_weight(vertices, edges):
    """Smallest total weight over all acyclic edge sets of size V - C."""
    size = len(vertices) - component_count(vertices, edges)
    return min(
        total(subset)
        for subset in itertools.combinations(edges, size)
        if is_forest(vertices, subset)
    )


def test_matches_brute_force_on_random_graphs():
    rng = random.Random(3)
    for _ in range(150):
        vertices = list(range(rng.randint(1, 6)))
        edges = [
            (u, v, rng.randint(1, 6))
            for u, v in itertools.combinations(vertices, 2)
            if rng.random() < 0.6
        ]
        tree = kruskal(vertices, edges)

        assert is_forest(vertices, tree)
        assert len(tree) == len(vertices) - component_count(vertices, edges)
        assert component_count(vertices, tree) == component_count(vertices, edges)
        assert total(tree) == brute_force_weight(vertices, edges)
