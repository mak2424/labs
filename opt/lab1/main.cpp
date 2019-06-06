#include <stdio.h>
#include <time.h>
#include <iostream>

#define SIZE 1024
#define BIGSIZE 2048
#define BLOCKSIZE 512

double F(double A, double B)
{
  double ret;
  ret = A * B;
  return ret;
}

void matmult_native(double* A, double* B, double* C, int size)
{
        for(int i = 0; i < size; i++)
                for(int j = 0; j < size; j++)
                        C[i*size + j] = 0.;
        for(int i = 0; i < size; i++)
                for(int j = 0; j < size; j++)
                        for(int k = 0; k < size; k++)
                                C[i*size + j] += F(A[i*size + k], B[k*size + j]);
}


int main()
{
    clock_t start, stop;	
    double*	A = new double [BIGSIZE*BIGSIZE];
    	double*	B = new double [BIGSIZE*BIGSIZE];
        double*	C = new double [BIGSIZE*BIGSIZE];

        for(int i = 0; i < BIGSIZE; i++)
    	    for(int j = 0; j < BIGSIZE; j++)
    		{
    			A[i*SIZE+j] = 0.1;
    			B[i*SIZE+j] = 1.1;
    		}
    printf("  native  matrix multiply ");
    start = clock();	
    matmult_native(A, B, C, SIZE);
    stop = clock();
    printf("native matmul  time = %lf seconds\n",((double)(stop - start)) / CLOCKS_PER_SEC);


    return 0;    
}
