# 68391447
"""Поиск расстояния до ближайшего свободного участка в строке с номерами домов.

Первая строка stdin - количество участков
Вторая строка stdin - список участков: нулевые значения - свободные участки,
ненулевые значения - номера домов.
"""

from typing import List

TEST_MODE = False
NULL_CHAR = '0'


def nearest_null(houses: List) -> List:
    """Функция поиска расстояния до ближайшего нуля.

    >>> nearest_null(['0', '1', '4', '9', '0'])
    [0, 1, 2, 1, 0]
    >>> nearest_null(['33', '44', '0', '55', '66', '77', '0', '0', '77'])
    [2, 1, 0, 1, 2, 1, 0, 0, 1]
    """
    count = 0
    divisor = 1
    for i, house_no in enumerate(houses):
        if house_no != NULL_CHAR:
            count += 1
            if divisor == 2:
                houses[i] = count
        else:
            houses[i] = 0
            for j in range(count // divisor):
                houses[i - (j + 1)] = j + 1
            count = 0
            divisor = 2
    return houses


if __name__ == '__main__':
    if not TEST_MODE:
        input()
        result = nearest_null(input().split())
        print(*result)
    else:
        import doctest
        doctest.testmod(verbose=True)
