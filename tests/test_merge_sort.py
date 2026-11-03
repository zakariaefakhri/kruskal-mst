import random

from kruskal import merge_sort


def test_sorts_by_key():
    edges = [("a", "b", 3), ("b", "c", 1), ("c", "d", 2)]
    assert merge_sort(edges, key=lambda e: e[2]) == [("b", "c", 1), ("c", "d", 2), ("a", "b", 3)]


def test_empty_and_single():
    assert merge_sort([], key=lambda x: x) == []
    assert merge_sort([5], key=lambda x: x) == [5]


def test_does_not_modify_input():
    items = [3, 1, 2]
    merge_sort(items, key=lambda x: x)
    assert items == [3, 1, 2]


def test_matches_sorted_and_is_stable():
    rng = random.Random(1)
    for _ in range(200):
        items = [(rng.randint(0, 5), i) for i in range(rng.randint(0, 30))]
        # sorted() is stable, so equal keys must keep their input order in both.
        assert merge_sort(items, key=lambda x: x[0]) == sorted(items, key=lambda x: x[0])
