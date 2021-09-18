
#include <stdio.h>

int main() {
  int num_1, num_2, max, min, n, ncicles, maxcicle;

  while(scanf("%d %d", &num_1, &num_2) != EOF) {
    maxcicle = 0;

    if (num_1 >= num_2) {
      min = num_2;
      max = num_1;
    } else {
      min = num_1;
      max = num_2;
    }

    for(int i = min; i <= max; i++) {
      n = i;
      ncicles = 0;

      while(1) {
        ncicles += 1;
        if (n == 1) {
          break;
        }
        if (n % 2 != 0) {
          n = 3 * n + 1;
        } else {
          n = n / 2;
        }
      }
      if (maxcicle < ncicles) {
        maxcicle = ncicles;
      }
    } 
    printf("%d %d %d\n", num_1, num_2, maxcicle);
  }
}