# Лабораторная работа  №4

### Результат выполнения:
## 3.
```
[sadaev.fan@n1 lab4]$  srun ./1.o
Enter matrix size N=500
roll_your_own_multiply(). Elapsed time = 1.7301 sec
Ddot_Multiply(). Elapsed time = 0.67045 sec
Dgemv_multiply(). Elapsed time = 0.0175999 sec
Dgemm_multiply(). Elapsed time = 0.0079631 sec

[sadaev.fan@n1 lab4]$  srun ./1.o
Enter matrix size N=1000
roll_your_own_multiply(). Elapsed time = 17.8604 sec
Ddot_Multiply(). Elapsed time = 4.49162 sec
Dgemv_multiply(). Elapsed time = 0.107139 sec
Dgemm_multiply(). Elapsed time = 0.0471578 sec

[sadaev.fan@n1 lab4]$ srun ./1.o
Enter matrix size N=2000
roll_your_own_multiply(). Elapsed time = 123.089 sec
Ddot_Multiply(). Elapsed time = 38.9682 sec
Dgemv_multiply(). Elapsed time = 13.1728 sec
Dgemm_multiply(). Elapsed time = 0.308432 sec

[sadaev.fan@n1 lab4]$ srun ./1.o
Enter matrix size N=4000
roll_your_own_multiply(). Elapsed time = 1066.66 sec
Ddot_Multiply(). Elapsed time = 444.488 sec
Dgemv_multiply(). Elapsed time = 122.34 sec
Dgemm_multiply(). Elapsed time = 2.28295 sec
```
## 6.
```
[sadaev.fan@n1 lab4]$ export MKL_NUM_THREADS=1
[sadaev.fan@n1 lab4]$ srun 2.o
Enter matrix size N=4000
 ....Elapsed time = 14.868 sec

[sadaev.fan@n1 lab4]$ export MKL_NUM_THREADS=2
[sadaev.fan@n1 lab4]$ srun 2.o
Enter matrix size N=4000
 ....Elapsed time = 7.50901 sec

[sadaev.fan@n1 lab4]$ export MKL_NUM_THREADS=3
[sadaev.fan@n1 lab4]$ srun 2.o
Enter matrix size N=4000
 ....Elapsed time = 7.51108 sec

[sadaev.fan@n1 lab4]$ export MKL_NUM_THREADS=4
[sadaev.fan@n1 lab4]$ srun 2.o
Enter matrix size N=4000
 ....Elapsed time = 3.78635 sec

[sadaev.fan@n1 lab4]$ export MKL_NUM_THREADS=5
[sadaev.fan@n1 lab4]$ srun 2.o
Enter matrix size N=4000
 ....Elapsed time = 3.79559 sec

[sadaev.fan@n1 lab4]$ export MKL_NUM_THREADS=6
[sadaev.fan@n1 lab4]$ srun 2.o
Enter matrix size N=4000
 ....Elapsed time = 3.00137 sec

[sadaev.fan@n1 lab4]$ export MKL_NUM_THREADS=7
[sadaev.fan@n1 lab4]$ srun 2.o
Enter matrix size N=4000
 ....Elapsed time = 3.04928 sec

[sadaev.fan@n1 lab4]$ export MKL_NUM_THREADS=8
[sadaev.fan@n1 lab4]$ srun 2.o
Enter matrix size N=4000
 ....Elapsed time = 2.30627 sec
```
## 7.
```
[sadaev.fan@n1 lab4]$ export MKL_VERBOSE=1
[sadaev.fan@n1 lab4]$ srun 2.o
Enter matrix size N=4000
MKL_VERBOSE Intel(R) MKL 2019.0 Update 3 Product build 20190125 for Intel(R) 64 architecture Intel(R) Supplemental Streaming SIMD Extensions 3 (Intel(R) SSSE3) enabled processors, Lnx 2.33GHz ilp64 gnu_thread
MKL_VERBOSE DGEMM(N,N,4000,4000,4000,0x7ffde4e62898,0x7f57d383e080,4000,0x7f57cbe2b080,4000,0x7ffde4e628a0,0x7f57c4418080,4000) 2.34s CNR:OFF Dyn:1 FastMM:1 TID:0  NThr:8
 ....Elapsed time = 2.33864 sec
```
## 8.
```
[sadaev.fan@n1 lab4]srun 3.o
Enter matrix size N=4000
Major version:           2019
Minor version:           0
Update version:          3
Product status:          Product
Build:                   20190125
Platform:                Intel(R) 64 architecture
Processor optimization:  Intel(R) Supplemental Streaming SIMD Extensions 3 (Intel(R) SSSE3) enabled processors
================================================================

MKL_VERBOSE Intel(R) MKL 2019.0 Update 3 Product build 20190125 for Intel(R) 64 architecture Intel(R) Supplemental Streaming SIMD Extensions 3 (Intel(R) SSSE3) enabled processors, Lnx 2.33GHz ilp64 gnu_thread
MKL_VERBOSE DGEMM(N,N,4000,4000,4000,0x7ffc55365e98,0x7f25ec64b080,4000,0x7f25e4c38080,4000,0x7ffc55365ea0,0x7f25dd225080,4000) 2.25s CNR:OFF Dyn:1 FastMM:1 TID:0  NThr:8
 ...Elapsed time = 2.24698 sec
```
## 9.
```
[sadaev.fan@n1 lab4]$ export MKL_ENABLE_INSTRUCTIONS=AVX512
[sadaev.fan@n1 lab4]srun 3.o
MKL_VERBOSE Intel(R) MKL 2019.0 Update 3 Product build 20190125 for Intel(R) 64 architecture Intel(R) Supplemental Streaming SIMD Extensions 3 (Intel(R) SSSE3) enabled processors, Lnx 2.33GHz ilp64 gnu_thread
MKL_VERBOSE DGEMM(N,N,4000,4000,4000,0x7fff4b79d508,0x7f60ffc57080,4000,0x7f60f8244080,4000,0x7fff4b79d510,0x7f60f0831080,4000) 2.28s CNR:OFF Dyn:1 FastMM:1 TID:0  NThr:8
 ...Elapsed time = 2.27654 sec



[sadaev.fan@n1 lab4]$ export MKL_VERBOSE=1
[sadaev.fan@n1 lab4]$ srun 3.o
Enter matrix size N=4000
Major version:           2019
Minor version:           0
Update version:          3
Product status:          Product
Update version:          3
Product status:          Product
Build:                   20190125
Platform:                Intel(R) 64 architecture
Processor optimization:  Intel(R) Supplemental Streaming SIMD Extensions 3 (Intel(R) SSSE3) enabled processors
================================================================

MKL_VERBOSE Intel(R) MKL 2019.0 Update 3 Product build 20190125 for Intel(R) 64 architecture Intel(R) Supplemental Streaming SIMD Extensions 3 (Intel(R) SSSE3) enabled processors, Lnx 2.33GHz ilp64 gnu_thread
MKL_VERBOSE DGEMM(N,N,4000,4000,4000,0x7ffe727c07d8,0x7f8e450f2080,4000,0x7f8e3d6df080,4000,0x7ffe727c07e0,0x7f8e35ccc080,4000) 2.33s CNR:OFF Dyn:1 FastMM:1 TID:0  NThr:8
 ...Elapsed time = 2.33427 sec

[sadaev.fan@n1 lab4]$ export MKL_ENABLE_INSTRUCTIONS=AVX
[sadaev.fan@n1 lab4]$ srun 3.o
Enter matrix size N=4000
Major version:           2019
Minor version:           0
Update version:          3
Product status:          Product
Build:                   20190125
Platform:                Intel(R) 64 architecture
Processor optimization:  Intel(R) Supplemental Streaming SIMD Extensions 3 (Intel(R) SSSE3) enabled processors
================================================================

MKL_VERBOSE Intel(R) MKL 2019.0 Update 3 Product build 20190125 for Intel(R) 64 architecture Intel(R) Supplemental Streaming SIMD Extensions 3 (Intel(R) SSSE3) enabled processors, Lnx 2.33GHz ilp64 gnu_thread
MKL_VERBOSE DGEMM(N,N,4000,4000,4000,0x7ffc811b5568,0x7fdec598c080,4000,0x7fdebdf79080,4000,0x7ffc811b5570,0x7fdeb6566080,4000) 2.25s CNR:OFF Dyn:1 FastMM:1 TID:0  NThr:8
 ...Elapsed time = 2.25455 sec

[sadaev.fan@n1 lab4]$ export MKL_ENABLE_INSTRUCTIONS=SSE4_2
[sadaev.fan@n1 lab4]$ srun 3.o
Enter matrix size N=4000
Major version:           2019
Minor version:           0
Update version:          3
Product status:          Product
Build:                   20190125
Platform:                Intel(R) 64 architecture
Processor optimization:  Intel(R) Supplemental Streaming SIMD Extensions 3 (Intel(R) SSSE3) enabled processors
================================================================

MKL_VERBOSE Intel(R) MKL 2019.0 Update 3 Product build 20190125 for Intel(R) 64 architecture Intel(R) Supplemental Streaming SIMD Extensions 3 (Intel(R) SSSE3) enabled processors, Lnx 2.33GHz ilp64 gnu_thread
MKL_VERBOSE DGEMM(N,N,4000,4000,4000,0x7ffddb8cbde8,0x7f812d186080,4000,0x7f8125773080,4000,0x7ffddb8cbdf0,0x7f811dd60080,4000) 2.26s CNR:OFF Dyn:1 FastMM:1 TID:0  NThr:8
 ...Elapsed time = 2.26114 sec
```

### Вопросы:
---
1. Сколько потоков MKL_NUM_THREADS устанавливает по умолчанию?
    > 1.
2. Какая зависимость времени вычисления от размера матрицы? (Линейная / экспоненциальная / логарифмическая)?
    > экспоненциальная
3. На что влияет параметр MKL_ENABLE_INSTRUCTIONS? Что такое наборы процессорных инструкций?
    > Разрешает диспетчеризацию для новых архитектур Intel® или ограничивает набор наборов инструкций Intel®, доступных для диспетчеризации. Набор процессорных инструкций ускоряет на аппаратном уровне какие-либо действия. Например инструкции, ускоряющие подсчет числа нулевых/единичных битов, комбинированные инструкции маскирования и сдвига, а также скалярные инструкции потоковой записи.
4. На что влияет параметр MKL_CBWR? 
    > Функция mkl_cbwr_set настраивает режим CNR. В этом выпуске он устанавливает ветвь CNR и включает режим CNR.