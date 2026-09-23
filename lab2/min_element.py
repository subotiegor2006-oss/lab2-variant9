"""Поиск минимального элемента списка.

Задание средней сложности №9.
"""

from typing import Sequence, TypeVar

T = TypeVar("T")


def find_min(items: Sequence[T]) -> T:
    """Вернуть минимальный элемент последовательности.

    Args:
        items: непустая последовательность сравнимых элементов.

    Raises:
        ValueError: если последовательность пуста.
    """
    if not items:
        raise ValueError("Список пуст")

    minimum = items[0]
    for item in items[1:]:
        if item < minimum:
            minimum = item
    return minimum


def find_min_index(items: Sequence[T]) -> int:
    """Вернуть индекс минимального элемента."""
    if not items:
        raise ValueError("Список пуст")

    min_idx = 0
    for i in range(1, len(items)):
        if items[i] < items[min_idx]:
            min_idx = i
    return min_idx


if __name__ == "__main__":
    examples = [
        [3, 1, 4, 1, 5, 9, 2, 6],
        [42],
        [-5, -1, -10, 0],
        ["banana", "apple", "cherry"],
    ]
    for seq in examples:
        print(f"{seq} → min = {find_min(seq)!r} (индекс {find_min_index(seq)})")
