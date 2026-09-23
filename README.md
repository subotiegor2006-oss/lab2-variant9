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

Демонстрация всех заданий:

```bash
python -m lab2
```

Отдельные модули:

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
├── __main__.py                 # точка входа
├── multiplication_table.py     # №1
├── calculator.py               # №6
├── min_element.py              # №9
├── euclid.py                   # №2 (повышенная)
└── recursive_sum.py            # №9 (повышенная)
tests/
└── test_lab2.py
```

## Примеры

```text
[№1] Таблица умножения 1..5
[№6] 15 + 7 = 22
[№9] min([8, 3, 15, 1, 9, 2]) = 1
[№2↑] НОД(48, 18) = 6
[№9↑] sum(1..100) = 5050
```
