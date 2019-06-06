#ifndef BITARRAY_H
#define BITARRAY_H

/* Abstract Data Type (ADT) representing an array of bits. Individual bits in the array can be
accessed through the accessor functions bitarray_get()/bitarray_set(). Additionally, some operations
that operate on substrings of bits are provided (bitarray_rotate() and bitarray_count_flips()). */

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>

typedef struct bitarray bitarray_t;

/* Allocate a new bitarray for storing bit_sz bits. */
bitarray_t *bitarray_new(size_t bit_sz);

/* Free a bitarray allocated by bitarray_new(). */
void bitarray_free(bitarray_t *ba);

/* Return the number of bits stored a bitarray, as given by the bit_sz argument to
bitarray_new(). */
size_t bitarray_get_bit_sz(bitarray_t *ba);

/* Index into the bitarray and retrieve the bit at the specified zero-based index. */
bool bitarray_get(bitarray_t *ba, size_t bit_index);

/* Index into the bitarray and set the bit at the specified zero-based index to the specified
value. */
void bitarray_set(bitarray_t *ba, size_t bit_index, bool val);

/* Выполняет операцию сдвига подстроки битов, индексация начинается с нуля между bit_off (включительно) и 
bit_off+bit_len (исключительно). Расстояние сдвига определено в bit_right_amount.
Положительные значения bit_right_amount сдвигают биты вправо, отрицательные влево.
Например, для сдвига всего массива битов 10010110 (сохраненного в массиве ba) влево
на один бит, выполните bitarray_rotate(ba, 0, bitarray_get_bit_sz(ba), -1); функция вернет 00101101.
Если выполнить bitarray_rotate(ba, 2, 5, 2) функция вернет 10110100. */
void bitarray_rotate(bitarray_t *ba, size_t bit_off, size_t bit_len, ssize_t bit_right_amount);


/* Считает количество битовых переходов в подстроке битов, индексация начинается 
с нуля между bit_off (включительно) и bit_off+bit_len (исключительно). Например, 
чтобы посчитать количество изменений битов во всем массиве битов 10010110, нужно вызвать
bitarray_count_flips(ba, 0, bitarray_get_bit_sz(ba)); функция вернет 5 (переходы отмечены точками
"1.00.1.0.11.0").*/
size_t bitarray_count_flips(bitarray_t *ba, size_t bit_off, size_t bit_len);


#endif /* BITARRAY_H */
