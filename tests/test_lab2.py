"""Unit-тесты лабораторной работы №2."""

import unittest

from lab2.multiplication_table import get_multiplication_table, print_multiplication_table
from lab2.calculator import calculate
from lab2.min_element import find_min, find_min_index
from lab2.euclid import gcd, gcd_recursive, lcm
from lab2.recursive_sum import recursive_sum, recursive_sum_range


class TestMultiplicationTable(unittest.TestCase):
    def test_table_5(self):
        table = get_multiplication_table(5)
        self.assertEqual(len(table), 5)
        self.assertEqual(table[0][0], 1)
        self.assertEqual(table[4][4], 25)
        self.assertEqual(table[2][3], 12)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            get_multiplication_table(0)


class TestCalculator(unittest.TestCase):
    def test_operations(self):
        self.assertEqual(calculate(10, "+", 3), 13)
        self.assertEqual(calculate(10, "-", 3), 7)
        self.assertEqual(calculate(10, "*", 3), 30)
        self.assertEqual(calculate(10, "/", 4), 2.5)
        self.assertEqual(calculate(10, "//", 3), 3)
        self.assertEqual(calculate(10, "%", 3), 1)
        self.assertEqual(calculate(2, "**", 8), 256)

    def test_div_zero(self):
        with self.assertRaises(ValueError):
            calculate(5, "/", 0)

    def test_unknown_op(self):
        with self.assertRaises(ValueError):
            calculate(1, "&", 2)


class TestMinElement(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(find_min([3, 1, 4, 1, 5]), 1)
        self.assertEqual(find_min_index([3, 1, 4, 1, 5]), 1)

    def test_single(self):
        self.assertEqual(find_min([42]), 42)

    def test_empty(self):
        with self.assertRaises(ValueError):
            find_min([])


class TestEuclid(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(17, 13), 1)
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(-36, 24), 12)

    def test_recursive(self):
        self.assertEqual(gcd_recursive(48, 18), 6)
        self.assertEqual(gcd_recursive(100, 25), 25)

    def test_lcm(self):
        self.assertEqual(lcm(12, 18), 36)
        self.assertEqual(lcm(0, 5), 0)


class TestRecursiveSum(unittest.TestCase):
    def test_list(self):
        self.assertEqual(recursive_sum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(recursive_sum([]), 0)
        self.assertEqual(recursive_sum([-3, 7, 1.5]), 5.5)

    def test_range(self):
        self.assertEqual(recursive_sum_range(10), 55)
        self.assertEqual(recursive_sum_range(0), 0)
        self.assertEqual(recursive_sum_range(1), 1)

    def test_negative(self):
        with self.assertRaises(ValueError):
            recursive_sum_range(-1)


if __name__ == "__main__":
    unittest.main()
