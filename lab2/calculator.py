"""Простой калькулятор.

Задание средней сложности №6.
"""

from typing import Union

Number = Union[int, float]


def calculate(a: Number, op: str, b: Number) -> Number:
    """Выполнить арифметическую операцию.

    Поддерживаемые операции: +, -, *, /, //, %, **.

    Raises:
        ValueError: при неизвестной операции или делении на ноль.
    """
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "//": lambda x, y: x // y,
        "%": lambda x, y: x % y,
        "**": lambda x, y: x ** y,
    }

    if op not in operations:
        raise ValueError(f"Неизвестная операция: {op!r}")

    if op in ("/", "//", "%") and b == 0:
        raise ValueError("Деление на ноль")

    return operations[op](a, b)


def run_calculator() -> None:
    """Интерактивный режим калькулятора."""
    print("Калькулятор. Введите выражение вида: 12 + 5")
    print("Доступные операции: + - * / // % **")
    print("Для выхода введите 'q'")

    while True:
        try:
            line = input("> ").strip()
            if line.lower() in ("q", "quit", "exit"):
                print("Выход.")
                break
            if not line:
                continue

            parts = line.split()
            if len(parts) != 3:
                print("Формат: число операция число")
                continue

            a = float(parts[0]) if "." in parts[0] else int(parts[0])
            op = parts[1]
            b = float(parts[2]) if "." in parts[2] else int(parts[2])

            result = calculate(a, op, b)
            print(f"= {result}")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Некорректный ввод: {e}")


if __name__ == "__main__":
    run_calculator()
