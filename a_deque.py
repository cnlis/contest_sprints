# 68493612
"""Модуль класса Deque.

Класс содержит методы, позволяющие добавлять и получать значения из начала
и конца дека за О(1)
"""

from typing import List, Optional, Union


ERROR_MSG = 'error'
TEST_MODE = False


class Deque:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def _inc(self, pointer: int) -> int:
        return (pointer + 1) % self.max_size

    def _dec(self, pointer: int) -> int:
        return (pointer - 1) % self.max_size

    def push_back(self, value: str) -> Optional[str]:
        if self.size == self.max_size:
            return ERROR_MSG
        self.queue[self.tail] = int(value)
        self.tail = self._inc(self.tail)
        self.size += 1

    def push_front(self, value: str) -> Optional[str]:
        if self.size == self.max_size:
            return ERROR_MSG
        self.head = self._dec(self.head)
        self.queue[self.head] = int(value)
        self.size += 1

    def pop_front(self) -> Union[str, int]:
        if not self.size:
            return ERROR_MSG
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = self._inc(self.head)
        self.size -= 1
        return value

    def pop_back(self) -> Union[str, int]:
        if not self.size:
            return ERROR_MSG
        self.tail = self._dec(self.tail)
        value = self.queue[self.tail]
        self.queue[self.tail] = None
        self.size -= 1
        return value

    @property
    def manager(self):
        return {
            'push_back': self.push_back,
            'push_front': self.push_front,
            'pop_front': self.pop_front,
            'pop_back': self.pop_back,
        }


def run_operations(deque_size: int, operations: List[str]):
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
    """
    deque = Deque(deque_size)
    for operation in operations:
        params = operation.split()
        result = deque.manager[params[0]](*params[1:])
        if result is not None:
            print(result)


if __name__ == '__main__':
    if not TEST_MODE:
        n = int(input())
        m = int(input())
        if n > 100000 or m > 50000:
            print(ERROR_MSG)
            exit()
        operations = [input() for _ in range(n)]
        run_operations(m, operations)
    else:
        import doctest
        doctest.testmod(verbose=True)
