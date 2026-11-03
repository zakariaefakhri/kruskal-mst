from .kruskal import Edge, kruskal

VERTICES = ["A", "B", "C", "D", "E"]
EDGES: list[Edge] = [
    ("A", "B", 2),
    ("A", "D", 3),
    ("A", "C", 1),
    ("A", "E", 2),
    ("B", "C", 3),
    ("C", "D", 8),
    ("D", "E", 5),
    ("C", "E", 1),
]


def show(title: str, vertices: list[str], edges: list[Edge]) -> None:
    tree = kruskal(vertices, edges)
    print(title)
    for u, v, weight in tree:
        print(f"  {u} - {v}  {weight}")
    print(f"  {len(tree)} edges, total weight {sum(weight for _, _, weight in tree)}")


def main() -> None:
    show("Minimum spanning tree:", VERTICES, EDGES)
    print()
    show(
        "Minimum spanning forest of a graph with two components:",
        VERTICES + ["X", "Y"],
        [*EDGES, ("X", "Y", 4)],
    )


if __name__ == "__main__":
    main()
