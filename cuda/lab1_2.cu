#include <iostream>
using namespace std;

int main () {
  int device_count;
  cudaGetDeviceCount(&device_count);

  cudaDeviceProp dp;

  cout << "CUDA device count: " << device_count << endl;

  for(int i = 0; i < device_count; i++) {
    cudaGetDeviceProperties(&dp, i);

    cout << i << ": " << dp.name << " with CUDA compute compatibility " << dp.major << "." << dp.minor << endl;
    cout << i << ": Тактовая частота ядра = " << dp.clockRate << endl;

    cout << "Память" << endl;
    cout << i << ": Общий объем графической памяти = " << dp.totalGlobalMem / 1024 / 1024 << endl;
    cout << i << ": Объем памяти констант = " << dp.totalConstMem << endl;
    cout << i << ": Максимальный шаг = " << dp.memPitch << endl;

    cout << "Мультипроцессоры" << endl;
    cout << i << ": Число потоковых мультипроцессоров = " << dp.multiProcessorCount << endl;
    cout << i << ": Объем разделяемой памяти в пределах блока = " << dp.sharedMemPerBlock << endl;
    cout << i << ": Число регистров в пределах блока = " << dp.regsPerBlock << endl;
    cout << i << ": Размер WARP’а (нитей в варпе) = " << dp.warpSize << endl;
    cout << i << ": Максимально допустимое число нитей в блоке = " << dp.maxThreadsPerBlock << endl;
    cout << i << ": Mаксимальную размерность при конфигурации нитей в блоке = " << dp.maxThreadsDim[0] << " " << dp.maxThreadsDim[1] << " " << dp.maxThreadsDim[2] << endl;
    cout << i << ": Максимальную размерность при конфигурации блоков в сетке = " << dp.maxGridSize[0] << " " << dp.maxGridSize[1] << " " << dp.maxGridSize[2] << endl;
  }

  return 0;
}