import os
import matplotlib.pyplot as plt
import random
import statistics
import math


def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './pictures/{}'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)


def z1_1():
    var = []
    avg_list = []
    err = []
    stand_err = []
    N = 1000
    a = 1/(N - 1)

    for i in range(N):
        var.append(random.random())
        avg = statistics.mean(var)  # среднее
        avg_list.append(avg)

        sum = 0.0

        for j in range(len(var)):
            sum += (var[j] - avg_list[i]) ** 2
        error_value=math.sqrt(a*sum)
        err.append(error_value)
        stand_err.append(error_value/math.sqrt(N))


    fig = plt.figure()
    plt.title('Задание 1')
    plt.ylabel('Среднее')
    plt.xlabel('Количество чисел')
    #graph1 = plt.plot(range(1000), avg_list)
    #print('Plot: ', len(graph1), graph1)
    plt.errorbar(range(1000), avg_list, yerr=stand_err, fmt='o-', ecolor='red')

    save(name='lab1', fmt='pdf')
    save(name='lab1', fmt='png')
    plt.show()


def z1_2():
    # Аналитическое решение
    red1 = (4 / 14) * (3 / 13)
    red2 = (3 / 14) * (2 / 13)
    red = red1 * red2
    black1 = (7 / 14) * (6 / 13)
    black2 = (3 / 14) * (2 / 13)
    black = black1 * black2
    blue1 = (3 / 14) * (2 / 13)
    blue2 = (8 / 14) * (7 / 13)
    blue = blue1 * blue2
    print(f"""
    Вероятность достать 2 красных шара из первой корзины: {red1}
    Вероятность достать 2 красных шара из второй корзины: {red2}
    Вероятность достать 2 чёрных шара из первой корзины: {black1}
    Вероятность достать 2 чёрных шара из второй корзины: {black2}
    Вероятность достать 2 синих шара из первой корзины: {blue1}
    Вероятность достать 2 синих шара из второй корзины: {blue2}
    
    Вероятность достать 4 красных шара из первой и второй корзины: {red}
    Вероятность достать 4 чёрных шара из первой и второй корзины: {black}
    Вероятность достать 4 синих шара из первой и второй корзины: {blue}
    
    Вероятность достать шары одинакового цвета: {red+black+blue}
    """)

    # Эксперименты
    def exp(n):
        experiment = []
        for i in range(n):
            box1 = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3]
            box2 = [0, 0, 0, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3]

            ball_1 = random.choice(box1)
            box1.remove(ball_1)
            ball_2 = random.choice(box1)

            ball_3 = random.choice(box2)
            box2.remove(ball_3)
            ball_4 = random.choice(box2)

            if ball_1 == ball_2 == ball_3 == ball_4:
                experiment.append(1)
            else:
                experiment.append(0)

        Mx = experiment.count(1) / len(experiment)

        D = 0
        for x in experiment:
            D += (x - Mx)
        D = D / len(experiment)

        print(f"Exp {n}: M={Mx} D={D}")

    exp(100)
    exp(500)
    exp(1000)
    exp(10000)


def z1_3():
    # Аналитическое решение
    print(f"""
        Отрезок АС: [0, 9]
        Отрезок СB: [5, 20]
        Пересечение где точка может быть по условию: [5, 9]
        Длина отрезка: 4
        Вероятность попадания: {4/20}
    """)

    # Эксперименты
    def exp(n):
        experiment = []
        for i in range(n):
            c = random.randint(0, 20)

            if 9 >= c >= 5:
                experiment.append(1)
            else:
                experiment.append(0)

        Mx = experiment.count(1) / len(experiment)

        D = 0
        for x in experiment:
            D += (x - Mx)
        D = D / len(experiment)

        print(f"Exp {n}: M={Mx} D={D}")

    exp(100)
    exp(500)
    exp(1000)
    exp(10000)

z1_3()