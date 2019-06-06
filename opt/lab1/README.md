# Лабораторная работа  №1

**Простой запуск:** native  matrix multiply native matmul  time = 75.030000 seconds

**O0:** native  matrix multiply native matmul  time = 75.560000 seconds

**O1:** native  matrix multiply native matmul  time = 64.380000 seconds

**O2:** native  matrix multiply native matmul  time = 65.650000 seconds

**O3:** native  matrix multiply native matmul  time = 64.070000 seconds

**O4:** native  matrix multiply native matmul  time = 64.890000 seconds

**O5:** native  matrix multiply native matmul  time = 63.680000 seconds

**O:** native  matrix multiply native matmul  time = 59.480000 seconds

---

1. Какой из уровней оптимизации -O0 ... -O5 оказался наиболее эффективным для нашей программы?
    - O5
2. Почему может случиться так, что более высокая оптимизация замедляет программу? Почему это случилось в случае с нашим кодом?
    - Может происходить излишняя оптимизация кода, например оптимизация функций которых в коде нет.
3. Определите какой конкретно параметр (или несколько параметров) оптимизации, включаемый командой -O негативно повлиял на время выполнения.
    - Команда: *g++ -O3 -fno-tree-fre  -fno-tree-dce  -fno-tree-copy-prop -fno-forward-propagate -fno-tree-ch -fno-tree-dominator-opts  main.cpp -o base.o* привела к улучшению результата *native  matrix multiply native matmul  time = 59.440000 seconds*