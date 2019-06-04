import random

MATRIX_LENGTH = 5
J = -1 #  тип взаимодействия, определяющий основные характеристики системы.


def init_matrix(matrix_length=MATRIX_LENGTH):
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
    string = ""
    for height in range(0, len(matrix)):
        for width in range(0, len(matrix[0])):
            string += f"{width}{height} {matrix[width][height]}\t"
        string += "\n"

    print(string)


def calculate_energy(matrix):
    E = 0
    matrix_length = len(matrix)
    for height in range(0, matrix_length):
        for width in range(0, len(matrix[0])):
            right = width + 1 if width + 1 < matrix_length else 0
            down = height + 1 if height + 1 < matrix_length else 0
            E += J * matrix[width][height] * matrix[right][height]
            E += J * matrix[width][height] * matrix[width][down]
    return E


matrix_S = init_matrix()
print(calculate_energy(matrix_S))