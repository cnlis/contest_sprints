# 68788997
"""Сортировка таблицы результатов участников соревнований.

Входные данные:
- первая строка: количество записей n
- следующие n строк: [имя] [количество выполненных заданий] [штраф]
Сортировка осуществляется сначала по количеству выполненных заданий по
убыванию, затем по штрафу по возрастанию, затем по имени по алфавиту.
"""
from typing import List, NamedTuple

TEST_MODE = False


class Record(NamedTuple):
    score: int
    penalty: int
    name: str


def partition(arr: List[Record], left: int, right: int) -> (int, int):
    """Сортировка массива относительно выбранного опорного значения."""
    mid = (left + right) // 2
    pivot = sorted((arr[left], arr[mid], arr[right]))[1]
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left, right


def quick_sort(arr: List[Record], left: int, right: int) -> None:
    """Алгоритм быстрой сортировки без дополнительной памяти."""
    if left >= right:
        return
    l_index, r_index = partition(arr, left, right)
    quick_sort(arr, left, r_index)
    quick_sort(arr, l_index, right)


def test():
    a = [1, 2, 3, 4, 5, 9, 10, 1, 2, 6]
    quick_sort(a, 0, len(a)-1)
    assert a == [1, 1, 2, 2, 3, 4, 5, 6, 9, 10]

    a = [(-4, 100, 'alla'), (-6, 1000, 'gena'), (-2, 90, 'gosha'),
         (-2, 90, 'rita'), (-4, 80, 'timofey')]
    quick_sort(a, 0, len(a)-1)
    assert a == [(-6, 1000, 'gena'), (-4, 80, 'timofey'), (-4, 100, 'alla'),
                 (-2, 90, 'gosha'), (-2, 90, 'rita')]

    a = [(0, 0, 'alla'), (0, 0, 'gena'), (0, 0, 'gosha'),
         (0, 0, 'rita'), (0, 0, 'timofey')]
    quick_sort(a, 0, len(a)-1)
    assert a == [(0, 0, 'alla'), (0, 0, 'gena'), (0, 0, 'gosha'),
                 (0, 0, 'rita'), (0, 0, 'timofey')]


if __name__ == '__main__':
    if not TEST_MODE:
        n = int(input())
        lst = []
        for _ in range(n):
            name, score, penalty = input().split()
            lst.append(Record(-int(score), int(penalty), name))
        quick_sort(lst, 0, len(lst)-1)
        for person in lst:
            print(person.name)
    else:
        test()
