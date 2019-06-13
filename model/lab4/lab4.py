import random
import statistics
import math
import matplotlib.pyplot as plt
import os
import time
import numpy as np
from matplotlib.animation import FuncAnimation
import copy

MATRIX_LENGTH = 4  # L - количество спинов вдоль одной сторо-ны квадрата
J = 1  # J - тип взаимодействия, определяющий основные характеристики системы.
SWAP_COUNT = 1000 * MATRIX_LENGTH * MATRIX_LENGTH  # m - выбор спина m раз


def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './pictures/'
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)


def init_matrix(matrix_length=MATRIX_LENGTH):
    """
    Генерирует случайную матрицу.

    :param int matrix_length: Длина матрицы
    :return: Возвращает сгенерированную матрицу.
    :rtype: list[list[int]]
    """
    new_matrix = []
    values = [1, -1]
    for height in range(0, matrix_length):
        inner_matrix = []
        for width in range(0, matrix_length):
            inner_matrix.append(random.choice(values))
        new_matrix.append(inner_matrix)

    print_matrix(new_matrix)
    return new_matrix


def print_matrix(matrix):
    """
    Выводит матрицу в консоль.

    :param list[list[int]] matrix: Матрица.
    """
    string = ""
    for height in range(0, len(matrix)):
        for width in range(0, len(matrix[0])):
            string += f"{width}{height} {matrix[width][height]}\t"
        string += "\n"

    print(string)


def calculate_energy(matrix):
    """
    Расчитывает энергию матрицы.

    :param list[list[int]] matrix: Матрица.
    :return: Возвращает энергию матрицы.
    :rtype: int
    """
    e = 0
    matrix_length = len(matrix)
    for height in range(0, matrix_length):
        for width in range(0, len(matrix[0])):
            right = width + 1 if width + 1 < matrix_length else 0
            down = height + 1 if height + 1 < matrix_length else 0
            e += -J * matrix[width][height] * matrix[right][height]
            e += -J * matrix[width][height] * matrix[width][down]
    return e


def calculate_energy_fast(e_old, width, height, matrix):
    """
    Расчитывает энергию матрицы.

    :param int e_old: Предыдущая энергия
    :param int width: положение x
    :param int height: положение y
    :param list[list[int]] matrix: Матрица.
    :return: Возвращает энергию матрицы.
    :rtype: int
    """
    matrix_length = len(matrix)
    right = width + 1 if width + 1 < matrix_length else 0
    left = width - 1 if width - 1 >= 0 else matrix_length - 1
    down = height + 1 if height + 1 < matrix_length else 0
    up = height - 1 if height - 1 >= 0 else matrix_length - 1
    s_j = matrix[right][height] + matrix[left][height] + matrix[width][down] + matrix[width][up]
    return e_old + (2 * -J * matrix[width][height] * s_j)


def find_min_conf(matrix_length=MATRIX_LENGTH):
    """
    Находит минимум энергии перебром всех конфигураций.

    :param int matrix_length: Длина матрицы
    """
    # Перебор
    matrix = []
    for height in range(0, matrix_length):
        inner_matrix = []
        for width in range(0, matrix_length):
            inner_matrix.append(-1)
        matrix.append(inner_matrix)

    min_e = calculate_energy(matrix)
    while matrix[matrix_length-1][matrix_length-1] < 2:
        val = calculate_energy(matrix)
        if min_e > val:
            min_e = val
            # print_matrix(matrix)
        matrix[0][0] += 2
        for height in range(0, matrix_length):
            for width in range(0, matrix_length):
                if matrix[width][height] > 1:
                    next_height = height + 1 if width + 1 >= matrix_length else height
                    next_width = width + 1 if next_height == height else 0
                    if next_height < matrix_length:
                        matrix[width][height] = -1
                        matrix[next_width][next_height] += 2
    print(f"Min brut: {min_e}")


def z4(matrix, T_min, T_max, step):
    e = calculate_energy(matrix)

    t_e = {}
    t_e2 = {}
    t = T_max
    while t > T_min:
        avr_e = []
        avr_e2 = []
        for i in range(0, SWAP_COUNT):
            old_e = e

            width = random.randint(0, len(matrix)-1)
            height = random.randint(0, len(matrix)-1)
            matrix[width][height] = -matrix[width][height]

            e = calculate_energy_fast(old_e, width, height, matrix)

            if e - old_e > 0:
                p = min([1, math.exp(-(e - old_e) / t)])
                p1 = random.random()
                if p1 > p:
                    matrix[width][height] = -matrix[width][height]
                    e = old_e

            avr_e.append(e)
            avr_e2.append(e ** 2)
        t_e[t] = statistics.mean(avr_e)
        t_e2[t] = statistics.mean(avr_e2)
        t -= step

    # e_average = statistics.mean(avr_e)
    # e_average2 = statistics.mean(avr_e2)
    print(f"Min metro: {e}")
    # print(f"Avg metro: {e_average}")
    # print(f"Avg2 metro: {e_average2}")
    return t_e, t_e2


temp = [t*0.1 for t in range(1, 50)]
start_time = time.time()
matrix_S = init_matrix()
T, T2 = z4(matrix_S, 0.1, 5, 0.1)
print(f"--- {(time.time() - start_time)} seconds ---")

fig1 = plt.figure()
plt.title(f'Лаб №4 <E>')
plt.ylabel('E')
plt.xlabel('T')
plt.plot(list(T.keys()), list(T.values()))
save(f"lab2-1", fmt='png')
plt.show()

fig1 = plt.figure()
plt.title(f'Лаб №4 <E2>')
plt.ylabel('E')
plt.xlabel('T')
plt.plot(list(T2.keys()), list(T2.values()))
save(f"lab2-2", fmt='png')
plt.show()