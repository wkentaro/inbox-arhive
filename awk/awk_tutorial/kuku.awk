#!/usr/bin/env awk -f

BEGIN {
  for (i=0; i<10; i++) {
    for (j=0; j<10; j++) {
      printf("%3d", i * j);
    }
    printf("\n");
  }
}