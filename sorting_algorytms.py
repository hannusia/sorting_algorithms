"""
This module contains implementations of different sorting algorytms.
"""


def selection_sort(array: list) -> int:
    comparisons = 0
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[min_index] < array[j]:
                min_index = j
            comparisons += 1
        array[i], array[min_index] = array[min_index], array[i]
    return comparisons


def insertion_sort(array: list) -> int:
    comparisons = 0
    for index in range(1, len(array)):
        current_value = array[index]
        position = index
        while position > 0 and array[position - 1] > current_value:
            comparisons += 1
            array[position] = array[position - 1]
            position = position - 1
        comparisons += 1
        array[position] = current_value
    return comparisons


def merge_sort(array: list) -> int:
    comparisons = 0
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        comparisons += merge_sort(left_half)
        comparisons += merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            comparisons += 1
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i = i + 1
            else:
                array[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            array[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            array[k] = right_half[j]
            j = j + 1
            k = k + 1
    return comparisons


def shell_sort(array: list) -> int:
    def __shell_sort(array: list) -> int:
        comparisons = 0
        sublist_count = len(array) // 2
        while sublist_count > 0:
            for start_position in range(sublist_count):
                comparisons += gap_insertion_sort(array, start_position, sublist_count)
            sublist_count = sublist_count // 2
        return comparisons

    def gap_insertion_sort(array: list, start: int, gap: int) -> int:
        comparisons = 0
        for i in range(start + gap, len(array), gap):
            current_value = array[i]
            position = i
            while position >= gap and array[position - gap] > current_value:
                comparisons += 1
                array[position] = array[position - gap]
                position = position - gap
            array[position] = current_value
            comparisons += 1
        return comparisons

    return __shell_sort(array)
