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


def z2():
    var4 = (0.079+0.209+0.375+0.337) * 0.079
    var3 = (0.209 + 0.337)*0.209
    var2 = (0.337 + 0.375)*0.375
    var1 = 0.337*0.337
    print(f""" 
    Вероятность найти донора при четвёртой группе крови: {var4}
    Вероятность найти донора при третьей группе крови: {var3}
    Вероятность найти донора при второй группе крови: {var2}
    Вероятность найти донора при первой группе крови: {var1}

    Вероятность того, что случайно взятому больному можно перелить кровь случайно взятого донора: {var1+var2+var3+var4}
    """)

    events = [0.337, 0.375, 0.209, 0.079]
    allias = [-1, -1, -1, -1]
    parts = events.copy()

    def init_alias():
        init_var = sum(events)/len(events)
        for var in range(len(events) - 1):
            max_value = max(events)
            max_index = events.index(max_value)
            min_value = min(events)
            min_index = events.index(min_value)


            diff = init_var - min_value
            #print(f"{max_value} {min_value} {diff}")
            events[min_index] = events[min_index] + diff
            allias[min_index] = max_index
            events[max_index] = events[max_index] - diff
            parts[max_index] = parts[max_index] - diff

    def generate_value():
        indx = random.randint(0, 3)
        if allias[indx] == -1:
            return indx

        u_value = random.random()
        if u_value > parts[indx]:
            return allias[indx]
        else:
            return indx

    def exp(n):
        init_alias()
        experiment = []
        select_blood = []
        for i in range(n):
            people1 = generate_value() + 1  # донор
            select_blood.append(str(people1))
            people2 = generate_value() + 1  # больной
            select_blood.append(str(people2))

            if people2 == 4:
                experiment.append(1)
            elif people2 == 3 and (people1 == 1 or people1 == 3):
                experiment.append(1)
            elif people2 == 2 and (people1 == 1 or people1 == 2):
                experiment.append(1)
            elif people2 == 1 and people1 == 1:
                experiment.append(1)
            else:
                experiment.append(0)

        Mx = experiment.count(1) / len(experiment)

        D = 0
        for x in experiment:
            D += (x - Mx)
        D = D / len(experiment)

        print(f"Exp {n}: M={Mx} D={D}")

        return select_blood

    data1 = exp(100)
    data2 = exp(500)
    data3 = exp(1000)
    exp(10000)

    fig1 = plt.figure()
    plt.title('Задание 2: 100')
    plt.ylabel('Количество событий')
    plt.xlabel('Группа крови')
    plt.hist([data1])
    save("lab2-2(100)", fmt='png')
    plt.show()

    fig1 = plt.figure()
    plt.title('Задание 2: 500')
    plt.ylabel('Количество событий')
    plt.xlabel('Группа крови')
    plt.hist([data2])
    save("lab2-2(500)", fmt='png')
    plt.show()

    fig1 = plt.figure()
    plt.title('Задание 2: 1000')
    plt.ylabel('Количество событий')
    plt.xlabel('Группа крови')
    plt.hist([data3])
    save("lab2-2(1000)", fmt='png')
    plt.show()


z1()
z2()
