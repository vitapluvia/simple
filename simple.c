#include <stdio.h>


int main(int argc, char** argv)
{
  if (!strcmp(argv[1], "a")) {
    printf("WIN!\n");
  } else {
    printf("lose...\n");
  }
}

