# 68493717
"""Обратная польская нотация.

Содержит функцию calculate, вычисляющую выражение, записанное в обратной
польской нотации.
"""

from typing import List

TEST_MODE = False


def calculate(operands: List[str]) -> int:
    """Вычисляет выражение, переданное в списке operands.

    Поддерживаемые операции: +, -, *, /
    Операция деления выполняется целочисленно.
    >>> calculate(['2', '1', '+', '3', '*'])
    9
    >>> calculate(['7', '2', '+', '4', '*', '2', '+'])
    38
    >>> calculate(['10', '2', '4', '*', '-'])
    2
    """
    operations = {
        '+': lambda a, b: b + a,
        '-': lambda a, b: b - a,
        '*': lambda a, b: b * a,
        '/': lambda a, b: b // a,
    }
    stack = []
    for operand in operands:
        if operand.lstrip('-').isdigit():
            stack.append(int(operand))
        else:
            stack.append(operations[operand](stack.pop(), stack.pop()))
    return stack.pop()


if __name__ == '__main__':
    if not TEST_MODE:
        line = input().split()
        print(calculate(line))
    else:
        import doctest
        doctest.testmod(verbose=True)
