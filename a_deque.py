# 68510252
"""Модуль класса Deque.

Класс содержит методы, позволяющие добавлять и получать значения из начала
и конца дека за О(1)
"""

from collections.abc import Iterator
from typing import List, Optional

ERROR_MSG = 'error'
TEST_MODE = True


class Pointer:
    def __init__(self, max_size: int):
        self.value: int = 0
        self.max_size: int = max_size

    def __call__(self) -> int:
        return self.value

    def inc(self) -> None:
        self.value = (self.value + 1) % self.max_size

    def dec(self) -> None:
        self.value = (self.value - 1) % self.max_size


class Deque:
    def __init__(self, max_size: int):
        self.max_size: int = max_size
        self.queue: List[Optional[int]] = [None] * max_size
        self.head: Pointer = Pointer(max_size)
        self.tail: Pointer = Pointer(max_size)
        self.size: int = 0

    def __len__(self) -> int:
        return self.size

    def _is_empty(self) -> bool:
        return not len(self)

    def _is_full(self) -> bool:
        return len(self) >= self.max_size

    def push_back(self, value: str) -> None:
        if self._is_full():
            raise IndexError(ERROR_MSG)
        self.queue[self.tail()] = int(value)
        self.tail.inc()
        self.size += 1

    def push_front(self, value: str) -> None:
        if self._is_full():
            raise IndexError(ERROR_MSG)
        self.head.dec()
        self.queue[self.head()] = int(value)
        self.size += 1

    def pop_front(self) -> int:
        if self._is_empty():
            raise IndexError(ERROR_MSG)
        value = self.queue[self.head()]
        self.queue[self.head()] = None
        self.head.inc()
        self.size -= 1
        return value

    def pop_back(self) -> int:
        if self._is_empty():
            raise IndexError(ERROR_MSG)
        self.tail.dec()
        value = self.queue[self.tail()]
        self.queue[self.tail()] = None
        self.size -= 1
        return value


def run_operations(deque_size: int, operations: Iterator[str]):
    """Запуск списка операций над деком.

    >>> run_operations(4, ['push_front 861', 'push_front -819', 'pop_back', \
                           'pop_back'])
    861
    -819
    >>> run_operations(7, ['push_front -855', 'push_front 0', 'pop_back', \
                           'pop_back', 'push_back 844', 'pop_back', \
                           'push_back 823'])
    -855
    0
    844
    >>> run_operations(6, ['push_front -201', 'push_back 959', \
                           'push_back 102', 'push_front 20', 'pop_front', \
                           'pop_back'])
    20
    102
    >>> run_operations(1, ['pop_back'])
    error
    """
    deque = Deque(deque_size)
    for operation in operations:
        command, *args = operation.split()
        try:
            func = getattr(deque, command)
            result = func(*args)
            if result is not None:
                print(result)
        except (AttributeError, IndexError):
            print(ERROR_MSG)


if __name__ == '__main__':
    if not TEST_MODE:
        n = int(input())
        m = int(input())
        if n > 100000 or m > 50000:
            print(ERROR_MSG)
            exit()
        commands = (input() for _ in range(n))
        run_operations(m, commands)
    else:
        import doctest
        doctest.testmod(verbose=True)
