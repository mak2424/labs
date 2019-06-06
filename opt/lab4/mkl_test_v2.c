#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "mkl.h"

void init_arr(int N, double* a);

int main(int argc, char* argv[])
{
	double start, stop;
	int N;
	double* a;
	double* b;
	double* c;
	double alpha = 1.0;
	double beta  = 1.0;
	if(argc < 2)
	{
		printf("Enter matrix size N=");
		fflush(stdout);
		//please enter small number first to ensure that the 
		//multiplication is correct! and then you may enter 
		//a "reasonably" large number say like 500 or even 1000
		scanf("%d",&N);
	}
	else
	{
		N = atoi(argv[1]);
	}
	
	/********************************************************** 
		DGEMM Multiply	
	**********************************************************/
	a=(double*) mkl_malloc( sizeof(double)*N*N, 64 );
	b=(double*) mkl_malloc( sizeof(double)*N*N, 64 );
	c=(double*) mkl_malloc( sizeof(double)*N*N, 64 );
	init_arr(N,a);
	init_arr(N,b);

	/*		
		DGEMM way. The PREFERED way, especially for large matrices
		cblas_dgemm - computes a matrix-matrix product with general matrices.	
		void cblas_cgemm (const CBLAS_LAYOUT Layout, const CBLAS_TRANSPOSE transa, const CBLAS_TRANSPOSE transb, const MKL_INT m, const MKL_INT n, const MKL_INT k, const void *alpha, const void *a, const MKL_INT lda, const void *b, const MKL_INT ldb, const void *beta, void *c, const MKL_INT ldc);
	*/

	
	start = dsecnd();
		cblas_dgemm(CblasRowMajor,CblasNoTrans,CblasNoTrans,N,N,N,alpha,b,N,a,N,beta,c,N);
	stop = dsecnd();

	printf(" ....Elapsed time = %g sec\n", stop - start);
		
	mkl_free(a);
	mkl_free(b);
	mkl_free(c);

	return 0;
}
//initialize array with random data
void init_arr(int N, double* a)
{	
	int i,j;
	for (i=0; i< N;i++) {
		for (j=0; j<N;j++) {
			a[i*N+j] = (i+j+1)%10; //keep all entries less than 10. pleasing to the eye!
		}
	}
}



