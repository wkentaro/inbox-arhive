#include <iostream>
#include <assert.h>

const int N_PRIMES = 7;  // number of elements

int primes[N_PRIMES] = {2, 3, 5, 7, 11, 13, 17};

int main(int argc, char* argv[]) {
  int index = 10;

  assert(index < N_PRIMES);
  assert(index >= 0);
  std::cout << "The tentch prime is " << primes[index] << std::endl;
  return 0;
}