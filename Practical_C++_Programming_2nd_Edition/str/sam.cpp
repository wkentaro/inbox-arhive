#include <iostream>
#include <cstring>

char name[30];  // someone's name

int main(int argc, char* argv[]) {
  std::strcpy(name, "Sam");
  std::cout << "The name is " << name << std::endl;
  return 0;
}