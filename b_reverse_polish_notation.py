# 68510300
"""Обратная польская нотация.

Содержит функцию calculate, вычисляющую выражение, записанное в обратной
польской нотации.
"""

import inspect
import operator
from typing import List

TEST_MODE = False


class Stack:
    def __init__(self):
        self.items: List[int] = []

    def pop(self) -> int:
        return self.items.pop()

    def push(self, value: int) -> None:
        self.items.append(value)


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
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
    }
    stack = Stack()
    for operand in operands:
        if operand.lstrip('-').isdigit():
            stack.push(int(operand))
        else:
            func = operations[operand]
            args = [stack.pop() for _ in inspect.signature(func).parameters]
            stack.push(func(*reversed(args)))
    return stack.pop()


if __name__ == '__main__':
    if not TEST_MODE:
        line = input().split()
        print(calculate(line))
    else:
        import doctest
        doctest.testmod(verbose=True)
