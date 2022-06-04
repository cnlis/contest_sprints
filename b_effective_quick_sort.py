# 68781591
"""Сортировка таблицы результатов участников соревнований.

Входные данные:
- первая строка: количество записей n
- следующие n строк: [имя] [количество выполненных заданий] [штраф]
Сортировка осуществляется сначала по количеству выполненных заданий по
убыванию, затем по штрафу по возрастанию, затем по имени по алфавиту.
"""
from typing import Any, List

TEST_MODE = False


def quick_sort(arr: List[Any], left: int, right: int):
    """Алгоритм быстрой сортировки без дополнительной памяти."""
    if left >= right:
        return
    mid = (left + right) // 2
    pivot = sorted((arr[left], arr[mid], arr[right]))[1]
    l_index = left
    r_index = right
    while l_index <= r_index:
        while arr[l_index] < pivot:
            l_index += 1
        while arr[r_index] > pivot:
            r_index -= 1
        if l_index <= r_index:
            arr[l_index], arr[r_index] = arr[r_index], arr[l_index]
            l_index += 1
            r_index -= 1
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
            data = input().split()
            lst.append((-int(data[1]), int(data[2]), data[0]))
        quick_sort(lst, 0, len(lst)-1)
        for person in lst:
            print(person[2])
    else:
        test()
