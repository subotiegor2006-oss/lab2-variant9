"""Рекурсивная сумма чисел.

Задание повышенной сложности №9.
"""

from typing import Sequence


def recursive_sum(numbers: Sequence[int | float]) -> int | float:
    """Вычислить сумму элементов последовательности рекурсивно.

    Args:
        numbers: последовательность чисел.

    Returns:
        Сумма элементов. Для пустой последовательности возвращает 0.
    """
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])


def recursive_sum_range(n: int) -> int:
    """Сумма чисел от 1 до n включительно (рекурсивно).

    Raises:
        ValueError: если n < 0.
    """
    if n < 0:
        raise ValueError("n не может быть отрицательным")
    if n == 0:
        return 0
    return n + recursive_sum_range(n - 1)


if __name__ == "__main__":
    print("Сумма списка [1, 2, 3, 4, 5] =", recursive_sum([1, 2, 3, 4, 5]))
    print("Сумма от 1 до 10 =", recursive_sum_range(10))
    print("Сумма пустого списка =", recursive_sum([]))
    print("Сумма [-3, 7, 1.5] =", recursive_sum([-3, 7, 1.5]))
