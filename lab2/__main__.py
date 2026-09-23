"""Демонстрация всех заданий лабораторной работы №2."""

from lab2.multiplication_table import print_multiplication_table, get_multiplication_table
from lab2.calculator import calculate
from lab2.min_element import find_min, find_min_index
from lab2.euclid import gcd, gcd_recursive, lcm
from lab2.recursive_sum import recursive_sum, recursive_sum_range


def main() -> None:
    print("=" * 50)
    print("Лабораторная работа №2 — вариант 9")
    print("Субботин Егор Сергеевич, группа 221341")
    print("=" * 50)

    # №1 — таблица умножения
    print("\n[№1] Таблица умножения 1..5:")
    print_multiplication_table(5)

    # №6 — калькулятор
    print("\n[№6] Калькулятор:")
    examples = [(15, "+", 7), (20, "/", 4), (2, "**", 10), (17, "%", 5)]
    for a, op, b in examples:
        print(f"  {a} {op} {b} = {calculate(a, op, b)}")

    # №9 — минимум
    print("\n[№9] Минимальный элемент:")
    data = [8, 3, 15, 1, 9, 2]
    print(f"  {data} → min = {find_min(data)} (индекс {find_min_index(data)})")

    # №2 повышенная — Евклид
    print("\n[№2↑] Алгоритм Евклида:")
    print(f"  НОД(48, 18) = {gcd(48, 18)}")
    print(f"  НОД(17, 13) = {gcd_recursive(17, 13)} (рекурсивно)")
    print(f"  НОК(12, 18) = {lcm(12, 18)}")

    # №9 повышенная — рекурсивная сумма
    print("\n[№9↑] Рекурсивная сумма:")
    print(f"  sum([1, 2, 3, 4, 5]) = {recursive_sum([1, 2, 3, 4, 5])}")
    print(f"  sum(1..100) = {recursive_sum_range(100)}")

    print("\nГотово.")


if __name__ == "__main__":
    main()
