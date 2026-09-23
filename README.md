# Лабораторная работа №2

Субботин Егор Сергеевич, группа 221341, вариант 9, лабораторная №2.

## Задания варианта

Средняя сложность:

- №1 — таблица умножения
- №6 — калькулятор
- №9 — минимальный элемент списка

Повышенная сложность:

- №2 — алгоритм Евклида
- №9 — рекурсивная сумма чисел

## Запуск

```bash
python -m lab2
```

или по отдельности:

```bash
python -m lab2.multiplication_table
python -m lab2.calculator
python -m lab2.min_element
python -m lab2.euclid
python -m lab2.recursive_sum
```

## Тесты

```bash
python -m unittest discover -s tests -v
```

## Структура

```text
lab2/
├── __init__.py
├── __main__.py
├── multiplication_table.py   # задание №1
├── calculator.py             # задание №6
├── min_element.py            # задание №9
├── euclid.py                 # задание №2 (повышенная)
└── recursive_sum.py          # задание №9 (повышенная)
tests/
└── ...
```
