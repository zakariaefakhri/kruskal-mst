# Pseudocode

## Kruskal

```text
FUNCTION kruskal(vertices, edges):
    tree = []
    sorted_edges = MERGE_SORT(edges by weight)    // new list, input unchanged
    components = UnionFind(vertices)

    FOR (u, v, weight) IN sorted_edges:
        IF LENGTH(tree) = LENGTH(vertices) - 1:
            BREAK                                 // tree is complete
        IF components.find(u) != components.find(v):
            APPEND (u, v, weight) TO tree
            components.union(u, v)

    RETURN tree
```

## Union-find

```text
FUNCTION find(v):
    root = v
    WHILE parent[root] != root:
        root = parent[root]
    WHILE parent[v] != root:                      // path compression
        next = parent[v]
        parent[v] = root
        v = next
    RETURN root

FUNCTION union(v, u):
    a = find(v)
    b = find(u)
    IF a = b:
        RETURN false
    IF size[a] < size[b]:
        SWAP a, b
    parent[b] = a                                 // smaller tree goes below larger
    size[a] = size[a] + size[b]
    RETURN true
```

## Merge sort

```text
FUNCTION merge_sort(items, key):
    IF LENGTH(items) <= 1:
        RETURN copy of items
    left = merge_sort(first half of items, key)
    right = merge_sort(second half of items, key)

    merged = []
    WHILE left and right both have elements:
        IF key(first of left) <= key(first of right):   // <= keeps it stable
            MOVE first of left TO merged
        ELSE:
            MOVE first of right TO merged
    APPEND the rest of left and right TO merged
    RETURN merged
```
