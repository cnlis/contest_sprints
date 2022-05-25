# 68391362
"""Модуль определения количества очков в тренажере скоростной печати.

Первая строка stdin - количество нажимаемых клавиш одним участником.
Вторая-пятая строки stdin - строки с 4 символами: цифрами или точками. Цифры
обозначают номера кнопок, которые должны нажать участники.
PARTICIPANTS - количество участников.
"""
from collections import Counter

TEST_MODE = False
PARTICIPANTS = 2


def buttons_game(fingers: int, lines: str) -> int:
    """Определение максимального числа очков, которые получат участники.

    >>> buttons_game(3, '12312..22..22..2')
    2
    >>> buttons_game(4, '1111999911119911')
    1
    >>> buttons_game(4, '1111111111111111')
    0
    """
    fingers = fingers * PARTICIPANTS
    buttons = Counter(button for button in lines if button.isdigit())
    count = sum(1 for i in buttons if 0 < buttons[i] <= fingers)
    return count


if __name__ == '__main__':
    if not TEST_MODE:
        k = int(input())
        lines_input = ''.join(input() for i in range(4))
        result = buttons_game(k, lines_input)
        print(result)
    else:
        import doctest
        doctest.testmod(verbose=True)
