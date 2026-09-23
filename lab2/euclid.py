"""Алгоритм Евклида — НОД двух чисел.

Задание повышенной сложности №2.
"""


def gcd(a: int, b: int) -> int:
    """Найти наибольший общий делитель (НОД) двух чисел.

    Классический алгоритм Евклида через остаток от деления.
    Работает и с отрицательными числами (возвращает неотрицательный результат).
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a: int, b: int) -> int:
    """Рекурсивная версия алгоритма Евклида."""
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def lcm(a: int, b: int) -> int:
    """Наименьшее общее кратное (НОК) через НОД."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    pairs = [(48, 18), (17, 13), (0, 5), (100, 25), (-36, 24)]
    for x, y in pairs:
        print(f"НОД({x}, {y}) = {gcd(x, y)}  (рекурсивно: {gcd_recursive(x, y)})")
        print(f"НОК({x}, {y}) = {lcm(x, y)}")
        print()
