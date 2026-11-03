from kruskal import UnionFind


def test_elements_start_in_their_own_set():
    uf = UnionFind("abc")
    assert len({uf.find(v) for v in "abc"}) == 3


def test_union_merges_sets():
    uf = UnionFind("abcd")
    assert uf.union("a", "b") is True
    assert uf.union("c", "d") is True
    assert uf.find("a") == uf.find("b")
    assert uf.find("a") != uf.find("c")
    assert uf.union("b", "d") is True
    assert len({uf.find(v) for v in "abcd"}) == 1


def test_union_of_same_set_returns_false():
    uf = UnionFind([1, 2])
    uf.union(1, 2)
    assert uf.union(2, 1) is False


def test_long_chains_do_not_recurse():
    n = 100_000
    uf = UnionFind(range(n))
    for i in range(n - 1):
        uf.union(i + 1, i)
    assert uf.find(0) == uf.find(n - 1)
