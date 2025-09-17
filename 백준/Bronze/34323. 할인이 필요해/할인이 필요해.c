//34323

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int main(void) {
    int N, M = 0;
    long S = 0;

    scanf("%d %d %ld", &N, &M, &S);

    long plus_one = S * M;
    long discount = (M+1) * S * (100 - N) / 100;

    printf("%ld", plus_one < discount ? plus_one : discount);
    return 0;
}