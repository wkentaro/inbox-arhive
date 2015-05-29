#include <string>
#include <iostream>

int main(int argc, char* argv[]) {
  std::string line;  // input
  std::cout << "Enter a line: ";
  std::getline(std::cin, line);

  std::cout << "The length of the line is: " << line.length() << std::endl;
  return 0;
}