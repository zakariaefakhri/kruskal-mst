# Kruskal's Algorithm

Finds a minimum spanning tree (MST) of a weighted, undirected graph with Kruskal's
algorithm. The edge sort (merge sort) and the union-find structure are written by
hand.

## How it works

1. Sort the edges by weight with merge sort. The sort is stable, so edges with
   equal weight keep their input order.
2. Put every vertex into its own set in a union-find structure.
3. Go through the edges from lightest to heaviest. If the two endpoints are in
   different sets, the edge cannot close a cycle: add it to the tree and merge the
   two sets. Otherwise skip it.
4. Stop when the tree has `V - 1` edges or the edges run out.

The union-find uses path compression and union by size, so each `find` or `union`
costs amortized O(alpha(V)), where alpha is the inverse Ackermann function. Sorting
dominates, so the total running time is O(E log E), which is the same as
O(E log V). Memory is O(V + E).

If the graph is disconnected, the result is a minimum spanning forest with one tree
per component. Self-loops are skipped, and of several parallel edges only the
lightest can be used. An edge with a vertex that is not in the vertex list raises
`ValueError`. The input list is not modified.

The pseudocode is in [docs/pseudocode.md](docs/pseudocode.md).

## Quickstart

Requires Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m kruskal
```

Output:

```text
Minimum spanning tree:
  A - C  1
  C - E  1
  A - B  2
  A - D  3
  4 edges, total weight 7

Minimum spanning forest of a graph with two components:
  A - C  1
  C - E  1
  A - B  2
  A - D  3
  X - Y  4
  5 edges, total weight 11
```

Use it from your own code:

```python
from kruskal import kruskal

vertices = ["A", "B", "C", "D"]
edges = [("A", "B", 4), ("B", "C", 1), ("A", "C", 2), ("C", "D", 5), ("B", "D", 7)]
print(kruskal(vertices, edges))
# [('B', 'C', 1), ('A', 'C', 2), ('C', 'D', 5)]
```

## Project structure

```text
src/kruskal/
    kruskal.py      the algorithm
    union_find.py   disjoint-set structure
    merge_sort.py   stable merge sort used for the edges
    __main__.py     demo run by `python -m kruskal`
tests/              pytest suite
docs/pseudocode.md  pseudocode for all three parts
```

## Tests

```bash
pip install -e ".[dev]"
ruff check .
ruff format --check .
pytest
```

The tests check hand-worked graphs, edge cases (empty graph, disconnected graphs,
self-loops, parallel edges, ties, a 5000-vertex path), merge sort against
`sorted()`, and compare the MST weight with a brute-force search over all edge
subsets on 150 random graphs.

## License

MIT
