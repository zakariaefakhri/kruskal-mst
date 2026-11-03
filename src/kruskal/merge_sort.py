from collections.abc import Callable, Sequence
from typing import Any, TypeVar

T = TypeVar("T")


def merge_sort(items: Sequence[T], key: Callable[[T], Any]) -> list[T]:
    """Return a new list with items sorted by key, in O(n log n) time.

    The sort is stable: items with equal keys keep their input order.
    The input sequence is not modified.
    """
    if len(items) <= 1:
        return list(items)

    mid = len(items) // 2
    left = merge_sort(items[:mid], key)
    right = merge_sort(items[mid:], key)

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        # <= takes from the left half on ties, which keeps the sort stable.
        if key(left[i]) <= key(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
