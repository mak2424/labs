# Лабораторная работа  №3

### Результат выполнения:
```
[sadaev.fan@n1 lab3]$g++ -O main.cpp -o base.o -lgsl -lgslcblas -lm
[sadaev.fan@n1 lab3]$ srun -p ddr ./base.o
  native  matrix multiply native matmul  time = 16.510000 seconds
```

### Вопросы:
---
1. Какая из функций GSL наиболее подходит для перемножения матриц?
    > gsl_blas_dgemm
2. Какие ключи компилятора пришлось добавить для работы с GSL?
    > -lgsl -lgslcblas -lm
3. Как изменилась скорость выполнения программы при использовании GSL?
    > Увеличилась до 16 секунд.
4. Повлияет ли подключение openmp на скорость работы программы?
    > Нет, так как функция в которой использовалась openmp заменена функцией из библиотеки blas.