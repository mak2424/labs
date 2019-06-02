import os
import matplotlib.pyplot as plt
import random
import statistics
import math


def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './pictures/lab1/{}'.format(fmt)
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

    save(name='lab1-1', fmt='png')
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


def z1_4():
    # Аналитическое решение
    red = (9 / 25) * (16 / 24)
    blue = (12 / 25) * (13 / 24)
    white = (4 / 25) * (21 / 24)
    print(f"""
    Вероятность достать красный и не красный: {red}
    Вероятность достать синий и не синий: {blue}
    Вероятность достать белый и не белый: {white}
    Вероятность достать 2 шара разного цвета: {red+ blue + white}
    """)

    # Эксперименты
    def exp(n):
        experiment = []
        for i in range(n):
            box = [0, 0, 0, 0, 0, 0, 0, 0, 0,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   2, 2, 2, 2]

            ball_1 = random.choice(box)
            box.remove(ball_1)
            ball_2 = random.choice(box)

            if ball_1 != ball_2:
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


def z2_1_1():

    def puasson(lam, N):
        dict = {}
        for i in range(N):
            k = 0
            p = math.exp(-lam)
            x = random.uniform(0, 1)
            while x > p:
                x = x - p
                k += 1
                p = p * lam / k
            dict[k] = p

        sorted_dict = {}
        for key in sorted(dict):
            sorted_dict[key] = dict[key]
        return sorted_dict

    dict1 = puasson(1, 50)
    dict4 = puasson(4, 50)
    dict10 = puasson(10, 50)



    fig = plt.figure()
    plt.title('Задание 2.1.1')
    plt.ylabel('P(k)')
    plt.xlabel('k')
    plt.plot(list(dict1.keys()), list(dict1.values()))
    plt.plot(list(dict4.keys()), list(dict4.values()))
    plt.plot(list(dict10.keys()), list(dict10.values()))
    save(name='lab2-1', fmt='png')
    plt.show()


def z2_1_2():
    lam = 4.3
    k = 0
    k_list = []
    params = []
    dict = {}
    for i in range(50):
        k += 1
        fact = math.factorial(k)
        p = ((lam ** k)*math.exp(-lam))/fact
        dict[k] = p

    sorted_dict = {}
    for key in sorted(dict):
        sorted_dict[key] = dict[key]

    fig = plt.figure()
    plt.title('Задание 2.1.2')
    plt.ylabel('P(k)')
    plt.xlabel('k')
    plt.plot(list(sorted_dict.keys()), list(sorted_dict.values()))
    save(name='lab2-1-2', fmt='png')
    plt.show()


def z2_2():

    def rasp(nu, sigma , N):
        x_list = []
        p_list = []
        dict = {}
        for i in range(N):
            x = random.uniform(-5, 5)
            p = (1/(sigma * math.sqrt(math.pi * 2)))*math.exp(-(((x-nu)**2)/(2*(sigma**2))))
            x_list.append(x)
            p_list.append(p)
            dict[x] = p
        sorted_dict = {}
        for key in sorted(dict):
            sorted_dict[key] = dict[key]
        return sorted_dict

    xp1 = rasp(0, 0.2, 100)
    xp2 = rasp(0, 1, 100)
    xp3 = rasp(0, 5, 100)
    xp4 = rasp(-2, 0.5, 100)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.title('Задание 2.2')
    plt.ylabel('P(k)')
    plt.xlabel('k')
    ax.plot(list(xp1.keys()), list(xp1.values()))
    ax.plot(list(xp2.keys()), list(xp2.values()))
    ax.plot(list(xp3.keys()), list(xp3.values()))
    ax.plot(list(xp4.keys()), list(xp4.values()))
    save(name='lab2-2', fmt='png')
    plt.show()


z1_1()
z1_2()
z1_3()
z1_4()
z2_1_1()
z2_1_2()
z2_2()
