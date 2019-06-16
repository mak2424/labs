#include <gsl/gsl_blas.h>
#include <gsl/gsl_matrix.h>
#include <omp.h>
#include <stdio.h>
#include <time.h>
#include <iostream>

#define SIZE 1024
#define BIGSIZE 2048
#define BLOCKSIZE 512

double F(double A, double B)
{
  return A * B;
}

void matmult_native(double* A, double* B, double* C, int size)
{
	//#pragma omp parallel shared(A,B,C, size)
	{
		for (int i = 0; i < size; i++)	
                        for (int k = 0; k < size; k++)
                        {
                                C[i*size + k] = 0.0;
                                //#pragma omp for nowait
                                for (int j = 0; j < size; j++)
                                        C[i*size + j] += A[i*size + j] * B[j*size + k];
                        }
	}                                       
}


int main()
{
    clock_t start, stop;	
    double* A = new double [BIGSIZE*BIGSIZE];
    double* B = new double [BIGSIZE*BIGSIZE];
    double* C = new double [BIGSIZE*BIGSIZE];

    for(int i = 0; i < BIGSIZE; i++)
        for(int j = 0; j < BIGSIZE; j++)
        {
                A[i*SIZE+j] = 0.1;
                B[i*SIZE+j] = 1.1;
                C[i*SIZE+j] = 0.0;
        }
    printf("  native  matrix multiply ");
    start = clock();
    gsl_matrix_view Ag = gsl_matrix_view_array(A, BIGSIZE, BIGSIZE);
    gsl_matrix_view Bg = gsl_matrix_view_array(B, BIGSIZE, BIGSIZE);
    gsl_matrix_view Cg = gsl_matrix_view_array(C, BIGSIZE, BIGSIZE);
    gsl_blas_dgemm (CblasNoTrans, CblasNoTrans,
                  1.0, &Ag.matrix, &Bg.matrix,
                  0.0, &Cg.matrix);
    //matmult_native(A, B, C, SIZE);
    stop = clock();
    printf("native matmul  time = %lf seconds\n",((double)(stop - start)) / CLOCKS_PER_SEC);


    return 0;    
}
