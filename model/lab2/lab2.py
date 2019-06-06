import random
import statistics
import math

MATRIX_LENGTH = 4  # L - количество спинов вдоль одной сторо-ны квадрата
J = -1  # J - тип взаимодействия, определяющий основные характеристики системы.
SWAP_COUNT = 10000 * MATRIX_LENGTH * MATRIX_LENGTH  # m - выбор спина m раз
T = 0.0001


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
    E = 0
    matrix_length = len(matrix)
    for height in range(0, matrix_length):
        for width in range(0, len(matrix[0])):
            right = width + 1 if width + 1 < matrix_length else 0
            down = height + 1 if height + 1 < matrix_length else 0
            E += -J * matrix[width][height] * matrix[right][height]
            E += -J * matrix[width][height] * matrix[width][down]
    return E


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


def z2(matrix):
    """
    Расчёт энергии методом метрополиса. 2 Лабораторная работа.

    :param list[list[int]] matrix: Матрица.
    """
    e = calculate_energy(matrix)
    avr_e = []
    for i in range(0, SWAP_COUNT):
        old_e = e

        width = random.randint(0, len(matrix)-1)
        height = random.randint(0, len(matrix)-1)
        matrix[width][height] = -matrix[width][height]

        e = calculate_energy(matrix)

        p = math.exp((e-old_e)/T)
        p1 = random.random()
        if p1 < p:
            matrix[width][height] = -matrix[width][height]
            e = old_e
        avr_e.append(e)

    print(f"Min metro: {e}")
    print(f"Avg metro: {statistics.mean(avr_e)}")


T = 5
print(f"T={T}")
matrix_S = init_matrix()
find_min_conf()
z2(matrix_S)

T = 1
print(f"T={T}")
matrix_S = init_matrix()
find_min_conf()
z2(matrix_S)


T = 0.1
print(f"T={T}")
matrix_S = init_matrix()
find_min_conf()
z2(matrix_S)

