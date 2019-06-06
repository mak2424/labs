#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "mkl.h"

void init_arr(int N, double* a);
void mkl_version();

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

	mkl_version();

	/*		
 		DGEMM way. The PREFERED way, especially for large matrices
		cblas_dgemm - computes a matrix-matrix product with general matrices.	
		void cblas_cgemm (const CBLAS_LAYOUT Layout, const CBLAS_TRANSPOSE transa, const CBLAS_TRANSPOSE transb, const MKL_INT m, const MKL_INT n, const MKL_INT k, const void *alpha, const void *a, const MKL_INT lda, const void *b, const MKL_INT ldb, const void *beta, void *c, const MKL_INT ldc);
	*/
	
	start = dsecnd();
		cblas_dgemm(CblasRowMajor,CblasNoTrans,CblasNoTrans,N,N,N,alpha,b,N,a,N,beta,c,N);
	stop = dsecnd();

	printf(" ...Elapsed time = %g sec \n", stop - start);
		
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

void mkl_version()
{
    MKLVersion Version; 
    mkl_get_version(&Version);
    printf("Major version:           %d\n",Version.MajorVersion);
    printf("Minor version:           %d\n",Version.MinorVersion);
    printf("Update version:          %d\n",Version.UpdateVersion);
    printf("Product status:          %s\n",Version.ProductStatus);
    printf("Build:                   %s\n",Version.Build);
    printf("Platform:                %s\n",Version.Platform);
    printf("Processor optimization:  %s\n",Version.Processor);
    printf("================================================================\n");
    printf("\n");
}

/***********************************************************************************
MKL_ENABLE_AVX512 --> Intel® Advanced Vector Extensions 512 (Intel® AVX-512) on Intel® Xeon® processors.
MKL_ENABLE_AVX2   --> Intel® Advanced Vector Extensions 2 (Intel® AVX2).
MKL_ENABLE_AVX    --> Intel® Advanced Vector Extensions (Intel® AVX).
MKL_ENABLE_SSE4_2 --> Intel® Streaming SIMD Extensions 4-2 (Intel® SSE4-2)

Environment Variable:
MKL_ENABLE_INSTRUCTIONS=AVX512
MKL_ENABLE_INSTRUCTIONS=AVX2
MKL_ENABLE_INSTRUCTIONS=AVX
MKL_ENABLE_INSTRUCTIONS=SSE4_2

rintime function:
int mkl_enable_instructions (int isa);
isa == MKL_ENABLE_AVX512 or MKL_ENABLE_AVX2 or MKL_ENABLE_AVX or MKL_ENABLE_SSE4_2

*************************************************************************************/
