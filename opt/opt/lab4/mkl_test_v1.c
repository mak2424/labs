//Simple minded matrix multiply
//For timing the function dsecnd() is used which is an MKL support function.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "mkl.h"

void print_arr(int N, char * name, double* array);
void init_arr(int N, double* a);
void Dgemm_multiply(double* a,double*  b,double*  c, int N);
void Dgemv_multiply(double* a,double*  b,double*  c, int N);
void Ddot_Multiply(double* a,double*  b,double*  c, int N);
void roll_your_own_multiply(double* a,double*  b,double*  c, int N);

int main(int argc, char* argv[])
{
	double start, stop;
	int N;
	double* a;
	double* b;
	double* c;
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
	void* mkl_malloc (size_t alloc_size, int alignment); 
	Allocates an aligned memory buffer.
	***********************************************************/
	a=(double*) mkl_malloc( sizeof(double)*N*N, 64 );
	b=(double*) mkl_malloc( sizeof(double)*N*N, 64 );
	c=(double*) mkl_malloc( sizeof(double)*N*N, 64 );

	init_arr(N,a);
	init_arr(N,b);

	/********************************************************** 
		dsecnd() - returns elapsed time in seconds. 
		Use to estimate real time between two calls to this function.
	**********************************************************/
	start = dsecnd();   
		roll_your_own_multiply(a,b,c,N);
	stop = dsecnd();
	printf("roll_your_own_multiply(). Elapsed time = %g sec\n",
		stop - start);
		//print simple test case of data to be sure multiplication is correct
	if (N < 7) {
		print_arr(N,"a", a);
		print_arr(N,"b", b);
		print_arr(N,"c", c);
	}
	
	/********************************************************** 
	Frees the aligned memory buffer allocated by mkl_malloc/mkl_calloc.
	**********************************************************/
	mkl_free(a);
	mkl_free(b);
	mkl_free(c);

	/********************************************************** 
		DDOT multiply
	***********************************************************/
	a=(double*) mkl_malloc( sizeof(double)*N*N, 64 );
	b=(double*) mkl_malloc( sizeof(double)*N*N, 64 );
	c=(double*) mkl_malloc( sizeof(double)*N*N, 64 );
	init_arr(N,a);
	init_arr(N,b);

	
	start = dsecnd();
		Ddot_Multiply(a,b,c,N);
	stop = dsecnd();

	printf("Ddot_Multiply(). Elapsed time = %g sec \n", stop - start);
	//print simple test case of data to be sure multiplication is correct
	if (N < 7) {
		print_arr(N,"a", a);
		print_arr(N,"b", b);
		print_arr(N,"c", c);
	}
	mkl_free(a);
	mkl_free(b);
	mkl_free(c);


	/********************************************************** 
		DGEMV Multiply		
	**********************************************************/
	a=(double*) mkl_malloc( sizeof(double)*N*N, 64 );
	b=(double*) mkl_malloc( sizeof(double)*N*N, 64 );
	c=(double*) mkl_malloc( sizeof(double)*N*N, 64 );
	init_arr(N,a);
	init_arr(N,b);

	start = dsecnd();
		Dgemv_multiply(a,b,c,N);
	stop = dsecnd();

	printf("Dgemv_multiply(). Elapsed time = %g sec \n", stop - start);
	//print simple test case of data to be sure multiplication is correct
	if (N < 7) {
		print_arr(N,"a", a);
		print_arr(N,"b", b);
		print_arr(N,"c", c);
	}
	mkl_free(a);
	mkl_free(b);
	mkl_free(c);


	/********************************************************** 
		DGEMM Multiply	
	**********************************************************/
	a=(double*) mkl_malloc( sizeof(double)*N*N, 64 );
	b=(double*) mkl_malloc( sizeof(double)*N*N, 64 );
	c=(double*) mkl_malloc( sizeof(double)*N*N, 64 );
	init_arr(N,a);
	init_arr(N,b);

	start = dsecnd();
	Dgemm_multiply(a,b,c,N);
	stop = dsecnd();

	printf("Dgemm_multiply(). Elapsed time = %g sec \n", stop - start);
	//print simple test case of data to be sure multiplication is correct
	if (N < 7) {
		print_arr(N,"a", a);
		print_arr(N,"b", b);
		print_arr(N,"c", c);
	}

	mkl_free(a);
	mkl_free(b);
	mkl_free(c);

	return 0;
}

//Brute force way of matrix multiply
void roll_your_own_multiply(double* a,double*  b,double*  c, int N)
{
	int i, j, k;
	for (i = 0; i < N; i++) {
		for (j=0; j<N; j++) {
			for (k=0; k<N; k++) {
				c[N*i+j] += a[N*i+k] * b[N*k+j];
			}
		}
	}
}

/*
   cblas_ddot() computes a vector-vector dot product.
   double cblas_ddot (const MKL_INT n, const double *x, const MKL_INT incx, const double *y, const MKL_INT incy);
*/
void Ddot_Multiply(double* a,double*  b,double*  c, int N)
{	
	int i, j;
	int incx = 1;
	int incy = N;
	for (i = 0; i < N; i++) {
		for (j=0; j<N; j++) {
			c[N*i+j] = cblas_ddot(N,&a[N*i],incx,&b[j],incy);
		}
	}
}

/*
	cblas_dgemv - computes a matrix-vector product using a general matrix
	void cblas_dgemv (const CBLAS_LAYOUT Layout, const CBLAS_TRANSPOSE trans, const MKL_INT m, const MKL_INT n, const double alpha, const double *a, const MKL_INT lda, const double *x, const MKL_INT incx, const double beta, double *y, const MKL_INT incy);
*/
void Dgemv_multiply(double* a,double*  b,double*  c, int N)
{	
	int i;
	double alpha = 1.0, beta = 0.;
//	int incx = 1;
//	int incy = N;
	for (i = 0; i < N; i++) {
		cblas_dgemv(CblasRowMajor,CblasNoTrans,N,N,alpha,a,N,&b[i],N,beta,&c[i],N);

	}
}

//DGEMM way. The PREFERED way, especially for large matrices
/*
	cblas_dgemm - computes a matrix-matrix product with general matrices.	
	void cblas_cgemm (const CBLAS_LAYOUT Layout, const CBLAS_TRANSPOSE transa, const CBLAS_TRANSPOSE transb, const MKL_INT m, const MKL_INT n, const MKL_INT k, const void *alpha, const void *a, const MKL_INT lda, const void *b, const MKL_INT ldb, const void *beta, void *c, const MKL_INT ldc);
*/
void Dgemm_multiply(double* a,double*  b,double*  c, int N)
{	
//	int i;
	double alpha = 1.0, beta = 0.;
//	int incx = 1;
//	int incy = N;
	cblas_dgemm(CblasRowMajor,CblasNoTrans,CblasNoTrans,N,N,N,alpha,b,N,a,N,beta,c,N);
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

//print array to std out
void print_arr(int N, char * name, double* array)
{	
	int i,j;	
	printf("\n%s\n",name);
	for (i=0;i<N;i++){
		for (j=0;j<N;j++) {
			printf("%g\t",array[N*i+j]);
		}
		printf("\n");
	}
}




