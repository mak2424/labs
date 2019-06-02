import random

MATRIX_LENGTH = 5
J = -1 #  тип взаимодействия, определяющий основные характеристики системы.


def init_matrix(matrix_length=MATRIX_LENGTH):
    new_matrix = []
    for width in range(0, matrix_length):
        inner_matrix = []
        for height in range(0, matrix_length):
            inner_matrix.append(random.randint(0, 1))
        new_matrix.append(inner_matrix)

    print_matrix(new_matrix)
    return new_matrix

def print_matrix(matrix):
    string = ""
    for width in range(0, len(matrix)):
        for height in range(0, len(matrix[0])):
            string += f"{matrix[width][height]} "
        string += "\n"

    print(string)

def calculate_energy(matrix, j):
    pass

matrix_S = init_matrix()

