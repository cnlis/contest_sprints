# 68762946

def search(nums, target, left, right) -> int:
    """Поиск значения в смещенном упорядоченном массиве за O(log(n))."""
    if right <= left:
        return -1
    mid = (left + right) // 2
    if nums[left] == target:
        return left
    if nums[mid] == target:
        return mid
    # искомое число находится на возрастающем отрезке, или является экстремумом
    # на отрезке, имеющем смещение значений
    if (nums[left] < target < nums[mid]
            or (nums[left] > nums[mid]
                and ((nums[left] > target < nums[mid])
                     or (nums[left] < target > nums[mid])))):
        return search(nums, target, left, mid)
    return search(nums, target, mid+1, right)


def broken_search(nums, target) -> int:
    return search(nums, target, 0, len(nums))


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    arr = [5, 1]
    assert broken_search(arr, 1) == 1
    arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4]
    assert broken_search(arr, 14) == 9
    arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4]
    assert broken_search(arr, 0) == -1
    arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4]
    assert broken_search(arr, 7) == 2
    arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4]
    assert broken_search(arr, 1) == 10
    arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4]
    assert broken_search(arr, 14) == 9


if __name__ == '__main__':
    test()
