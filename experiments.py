"""
This module contains functions to sorting algorythms and collect data about experiments.
"""
from generate_array import *
from sorting_algorytms import *
from copy import deepcopy
import time


def experiment_1():
    result = []

    for power in range(10, 16):
        selection_t = 0
        selection_c = 0
        insertion_t = 0
        insertion_c = 0
        merge_t = 0
        merge_c = 0
        shell_t = 0
        shell_c = 0

        for _ in range(5):
            lst = generate_random(power)

            lst_1 = deepcopy(lst)
            start = time.time()
            selection_c += selection_sort(lst_1)
            selection_t += (time.time() - start)

            lst_2 = deepcopy(lst)
            start = time.time()
            insertion_c += insertion_sort(lst_2)
            insertion_t += (time.time() - start)

            lst_3 = deepcopy(lst)
            start = time.time()
            merge_c += merge_sort(lst_3)
            merge_t += (time.time() - start)

            lst_4 = deepcopy(lst)
            start = time.time()
            shell_c += shell_sort(lst_4)
            shell_t += (time.time() - start)

        result.append(('\t').join(['selection', str(power), str(
            int(selection_c / 5)), format(selection_t / 5, '.5f'), '\n']))
        result.append(('\t').join(['insertion', str(power), str(
            int(insertion_c / 5)), format(insertion_t / 5, '.5f'), '\n']))
        result.append(('\t').join(['merge', str(power), str(
            int(merge_c / 5)), format(merge_t / 5, '.5f'), '\n']))
        result.append(('\t').join(['shell', str(power), str(
            int(shell_c / 5)), format(shell_t / 5, '.5f'), '\n']))

    with open('results1.txt', 'a+') as file:
        file.writelines(result)
    return result


def experiment_234(exp: int) -> list:
    result = []

    for power in range(7, 16):
        print(power)

        if exp == 2:
            lst = generate_increasing(power)
        elif exp == 3:
            lst = generate_decreasing(power)
        else:
            lst = generate_from_set(power)

        selection_t = 0
        selection_c = 0
        insertion_t = 0
        insertion_c = 0
        merge_t = 0
        merge_c = 0
        shell_t = 0
        shell_c = 0

        lst_1 = deepcopy(lst)
        start = time.time()
        selection_c += selection_sort(lst_1)
        selection_t += (time.time() - start)

        lst_2 = deepcopy(lst)
        start = time.time()
        insertion_c += insertion_sort(lst_2)
        insertion_t += (time.time() - start)

        lst_3 = deepcopy(lst)
        start = time.time()
        merge_c += merge_sort(lst_3)
        merge_t += (time.time() - start)

        lst_4 = deepcopy(lst)
        start = time.time()
        shell_c += shell_sort(lst_4)
        shell_t += (time.time() - start)

        result.append(('\t').join(['selection', str(power), str(
            selection_c), format(selection_t, '.5f'), '\n']))
        result.append(('\t').join(['insertion', str(power), str(
            insertion_c), format(insertion_t, '.5f'), '\n']))
        result.append(('\t').join(
            ['merge', str(power), str(merge_c), format(merge_t, '.5f'), '\n']))
        result.append(('\t').join(
            ['shell', str(power), str(shell_c), format(shell_t, '.5f'), '\n']))

    with open(f'results{exp}.txt', 'a+') as file:
        file.writelines(result)
    return result
