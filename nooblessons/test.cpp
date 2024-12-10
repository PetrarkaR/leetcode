#include <hip/hip_runtime.h>
#include <iostream>

__global__ void add(int* a, int* b, int* c, int N) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < N) c[i] = a[i] + b[i];
}

int main() {
    int N = 1024;
    int *a, *b, *c;
    hipMallocManaged(&a, N * sizeof(int));
    hipMallocManaged(&b, N * sizeof(int));
    hipMallocManaged(&c, N * sizeof(int));
    
    for (int i = 0; i < N; i++) a[i] = b[i] = i;

    hipLaunchKernelGGL(add, dim3((N + 255) / 256), dim3(256), 0, 0, a, b, c, N);

    hipDeviceSynchronize();
    
    std::cout << "c[0] = " << c[0] << ", c[N-1] = " << c[N-1] << std::endl;

    hipFree(a);
    hipFree(b);
    hipFree(c);
    return 0;
}
