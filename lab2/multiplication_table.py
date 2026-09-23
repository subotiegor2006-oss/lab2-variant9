"""Таблица умножения.

Задание средней сложности №1.
"""


def print_multiplication_table(n: int = 10) -> None:
    """Вывести таблицу умножения от 1 до n.

    Args:
        n: верхняя граница (включительно). Должно быть >= 1.
    """
    if n < 1:
        raise ValueError("n должно быть положительным числом")

    for i in range(1, n + 1):
        row = " ".join(f"{i * j:4}" for j in range(1, n + 1))
        print(row)


def get_multiplication_table(n: int = 10) -> list[list[int]]:
    """Вернуть таблицу умножения как список списков."""
    if n < 1:
        raise ValueError("n должно быть положительным числом")
    return [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]


if __name__ == "__main__":
    print("Таблица умножения 1..10:")
    print_multiplication_table(10)
