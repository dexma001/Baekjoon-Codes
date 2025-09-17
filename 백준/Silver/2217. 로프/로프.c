//2217

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void* a, const void* b){
    return (*(int *)b - *(int *)a);
}

int main(void) {
    int N;
    scanf("%d", &N);
    int rope[N];

    for (int i = 0; i < N; i++) {
        int temp;
        scanf("%d", &temp);
        rope[i] = temp;
    }

    qsort(rope, N, sizeof(int), compare);

    long answer = 0;
    for (int i = 0; i < N; i++) {
        int is_max = rope[i] * (i + 1);
        if (is_max > answer) {
            answer = is_max;
        } 
    }

    printf("%ld", answer);
    return 0;
}