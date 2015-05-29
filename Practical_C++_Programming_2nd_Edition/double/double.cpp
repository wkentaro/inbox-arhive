#include <iostream>

int value;  // value to be twiced

int main(int argc, char* argv[]) {
  std::cout << "Enter a value: ";
  std::cin >> value;
  std::cout << "Twice " << value << " is " << value * 2 << std::endl;
  return 0;
}