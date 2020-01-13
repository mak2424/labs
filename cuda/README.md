# CUDA

## Лабраторная №1:

### **Задание №1**

[Код](lab1_1.cu)

Результат выполнения:
```
[fsadaev@jupiter5 cuda]$ nvcc lab1_1.cu --run
nvcc warning : The 'compute_20', 'sm_20', and 'sm_21' architectures are deprecated, and may be removed in a future release (Use -Wno-deprecated-gpu-targets to suppress warning).
Hello from CPU!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
```

### **Задание №2**

[Код](lab1_2.cu)

Результат выполнения:
```
[fsadaev@jupiter5 cuda]$ nvcc lab1_2.cu --run
nvcc warning : The 'compute_20', 'sm_20', and 'sm_21' architectures are deprecated, and may be removed in a future release (Use -Wno-deprecated-gpu-targets to suppress warning).
CUDA device count: 1
0: Tesla P100-SXM2-16GB with CUDA compute compatibility 6.0
0: Тактовая частота ядра = 1480500
Память
0: Общий объем графической памяти = 16280
0: Объем памяти констант = 65536
0: Максимальный шаг = 2147483647
Мультипроцессоры
0: Число потоковых мультипроцессоров = 56
0: Объем разделяемой памяти в пределах блока = 49152
0: Число регистров в пределах блока = 65536
0: Размер WARP’а (нитей в варпе) = 32
0: Максимально допустимое число нитей в блоке = 1024
0: Mаксимальную размерность при конфигурации нитей в блоке = 1024 1024 64
0: Максимальную размерность при конфигурации блоков в сетке = 2147483647 65535 65535
```

## Лабраторная №2:

### **Задание №1**

[Код](lab2_1.cu)

Результат выполнения:
```
[fsadaev@jupiter5 cuda]$ nvcc lab2_1.cu --run
nvcc warning : The 'compute_20', 'sm_20', and 'sm_21' architectures are deprecated, and may be removed in a future release (Use -Wno-deprecated-gpu-targets to suppress warning).
2 + 7 = 9
```

### **Задание №2**

[Код](lab2_2.cu)

Результат выполнения:
```
[fsadaev@jupiter5 cuda]$ nvcc lab2_2.cu --run
nvcc warning : The 'compute_20', 'sm_20', and 'sm_21' architectures are deprecated, and may be removed in a future release (Use -Wno-deprecated-gpu-targets to suppress warning).
Arrays:
3 5 6 1 0  5 7 7 4 7 
6 3 2 2 9  2 5 1 3 0 
7 5 9 7 3  1 4 0 6 7 

Max:
7 5 9 7 9  5 7 7 6 7 
```