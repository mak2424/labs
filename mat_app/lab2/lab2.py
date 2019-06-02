import os
import matplotlib.pyplot as plt
import random
import statistics
import math

def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './pictures/'
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)

def z1():
    print(f"""
    Вероятность выбора любого ящика: {1/3}
    Вероятность взять стандартную деталь в первом ящике: {15/20}
    Вероятность взять стандартную деталь во втором ящике: {24/30}
    Вероятность взять стандартную деталь в третьем ящике: {6/10}
    
    Вероятность  того, что наудачу извлеченная деталь из наудачу взятого ящика-стандартная: {(1/3)*((15/20)+
                                                                                                    (24/30)+
                                                                                                    (6/10))}
    """)

    # Эксперименты
    def exp(n):
        experiment = []
        select_box = {1: [], 2: [], 3: [], "box_select": []}
        for i in range(n):
            box_number = random.randint(1, 3)
            select_box["box_select"].append(str(box_number))
            if box_number == 1:
                detal = random.randint(1, 20)
                if detal <= 15:
                    experiment.append(1)
                    select_box[box_number].append("Выбрана стандартная деталь")
                else:
                    experiment.append(0)
                    select_box[box_number].append("Выбрана нестандартная деталь")

            elif box_number == 2:
                detal = random.randint(1, 30)
                if detal <= 24:
                    experiment.append(1)
                    select_box[box_number].append("Выбрана стандартная деталь")
                else:
                    experiment.append(0)
                    select_box[box_number].append("Выбрана нестандартная деталь")
            elif box_number == 3:
                detal = random.randint(1, 10)
                if detal <= 6:
                    experiment.append(1)
                    select_box[box_number].append("Выбрана стандартная деталь")
                else:
                    experiment.append(0)
                    select_box[box_number].append("Выбрана нестандартная деталь")

        Mx = experiment.count(1) / len(experiment)

        D = 0
        for x in experiment:
            D += (x - Mx)
        D = D / len(experiment)

        print(f"Exp {n}: M={Mx} D={D}")

        return select_box

    data1 = exp(100)
    data2 = exp(500)
    data3 = exp(1000)

    fig1 = plt.figure()
    plt.title('Задание 1: 100')
    plt.ylabel('Количество событий')
    plt.xlabel('События')
    plt.hist([data1[1], data1[2], data1[3]])
    save("lab2-1(100)", fmt='png')
    plt.show()

    fig1 = plt.figure()
    plt.title('Задание 1: 500')
    plt.ylabel('Количество событий')
    plt.xlabel('События')
    plt.hist([data2[1], data2[2], data2[3]])
    save("lab2-1(500)", fmt='png')
    plt.show()

    fig1 = plt.figure()
    plt.title('Задание 1: 1000')
    plt.ylabel('Количество событий')
    plt.xlabel('События')
    plt.hist([data3[1], data3[2], data3[3]])
    save("lab2-1(1000)", fmt='png')
    plt.show()

    fig1 = plt.figure()
    plt.title('Задание 1: Выбор коробки')
    plt.ylabel('Количество событий')
    plt.xlabel('События')
    plt.hist([data1["box_select"], data2["box_select"], data3["box_select"]])
    save("lab2-1(box)", fmt='png')
    plt.show()
z1()