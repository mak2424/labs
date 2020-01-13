#include <iostream>
using namespace std;

#define N 10000000

__global__ void add(int *a, int *b, int *c, int *result) {
    int tid = blockIdx.x * blockDim.x + threadIdx.x;
    int max = a[tid];


    if (tid < N) {
        if (b[tid] > max) {
            max = b[tid];
        }

        if (c[tid] > max) {
            max = c[tid];
        }

        result[tid] = max;
    }
}

void array_print(int *array, int count) {
    for(int i = 0; i < count * 2; i++) {
    if (i < count) {
        cout << "" << array[i] << " ";
    }

    if (i == count) {
        cout << " ";
    }

    if (i > count - 1 && i < count * 2) {
        cout << "" << array[N - (count * 2 - i) - 1] << " ";
    }
    }
    cout << endl;
}

int main(void) 
{
    int a[N], b[N], c[N], result[N];
    int *input_a, *input_b, *input_c, *out_result;

    int numThreadsPerBlock = 1000;
    int numBlocks = (N + numThreadsPerBlock - 1) / numThreadsPerBlock;

    cudaMalloc((void**)&input_a, N * sizeof(int));
    cudaMalloc((void**)&input_b, N * sizeof(int));
    cudaMalloc((void**)&input_c, N * sizeof(int));
    cudaMalloc((void**)&out_result, N * sizeof(int));

    for (int i = 0; i < N; i++) {
        a[i] = rand() % 10;
        b[i] = rand() % 10;
        c[i] = rand() % 10;
    }

    cudaMemcpy(input_a, a, N * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(input_b, b, N * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(input_c, c, N * sizeof(int), cudaMemcpyHostToDevice);

    add<<<numBlocks, numThreadsPerBlock>>>(input_a, input_b, input_c, out_result);

    cudaMemcpy(result, out_result, N * sizeof(int), cudaMemcpyDeviceToHost);

    cout << "Arrays:" << endl;

    array_print(a, 5);
    array_print(b, 5);
    array_print(c, 5);

    cout << endl << "Max:" << endl;

    array_print(result, 5);

    cudaFree(input_a);
    cudaFree(input_b);
    cudaFree(input_c);
    cudaFree(out_result);

    return 0;
}