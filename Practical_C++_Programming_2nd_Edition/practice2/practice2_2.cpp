#include <iostream>

int square(int x) { return x * x; }

int main(int argc, char* argv[]) {
  int x = 3;
  std::cout << "Square of " << x << " is " << square(3) << std::endl;
}