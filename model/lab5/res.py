import matplotlib.pyplot as plt
import os

def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './pictures/'
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)

file = open('res.txt', 'r')
x = []
y = []
for line in file:
    x.append(float(line.split(" ")[0]))
    y.append(float(line.split(" ")[2]))
file.close()

fig1 = plt.figure()
plt.title(f'Лаб №5 G')
plt.ylabel('G')
plt.xlabel('T')
plt.plot(x, y)
save(f"lab5-1", fmt='png')
plt.show()
