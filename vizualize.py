import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def read_file(path: str):
    result_time = {'selection': [], 'insertion': [], 'merge': [], 'shell': []}
    result_compares = {'selection': [],
                       'insertion': [], 'merge': [], 'shell': []}
    with open(path) as file:
        lines = file.read().splitlines()
    for line in lines:
        line_s = line.split('\t')
        result_time[line_s[0]].append(float(line_s[3]))
        result_compares[line_s[0]].append(int(line_s[2]))
    return result_compares, result_time


def vizualize(path: str, label: str):
    fig_1, ax_1 = plt.subplots()
    fig_2, ax_2 = plt.subplots()

    x = [2**7, 2**8, 2**9, 2**10, 2**11, 2**12, 2**13, 2**14, 2**15]

    coord = read_file(path)

    ax_1.plot(x, coord[1]['shell'], color='red', label='shell sort', marker='o')
    ax_1.plot(x, coord[1]['merge'], color='yellow', label='merge sort', marker='o')
    ax_1.plot(x, coord[1]['selection'], color='blue', label='selection sort', marker='o')
    ax_1.plot(x, coord[1]['insertion'], color='green', label='insertion sort', marker='o')
    ax_1.set_xscale('log')
    ax_1.set_yscale('log')
    ax_1.set_title(label)
    ax_1.set_xlabel('К-ть елементів в масиві')
    ax_1.set_ylabel('Час сортування')
    ax_1.legend(loc='upper left')

    ax_2.plot(x, coord[0]['shell'], color='red', label='shell sort', marker='o')
    ax_2.plot(x, coord[0]['merge'], color='yellow', label='merge sort', marker='o')
    ax_2.plot(x, coord[0]['selection'], color='blue', label='selection sort', marker='o')
    ax_2.plot(x, coord[0]['insertion'], color='green', label='insertion sort', marker='o')
    ax_2.set_xscale('log')
    ax_2.set_yscale('log')
    ax_2.set_title(label)
    ax_2.set_xlabel('К-ть елементів в масиві')
    ax_2.set_ylabel('К-ть порівнянь')
    ax_2.legend(loc='upper left')

    name_1 = f'exp{path[7]}_t.jpg'
    name_2 = f'exp{path[7]}_c.jpg'
    fig_1.savefig(name_1)
    fig_2.savefig(name_2)


vizualize('results4.txt', 'Результати ексерименту №4')
