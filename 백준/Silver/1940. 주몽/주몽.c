//1940

#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b){
    return (*(long *)a - *(long *)b);
}

int main(void){
    long N, M;
    scanf("%ld", &N);
    scanf("%ld", &M);

    long arr[N];
    for (int i = 0; i < N; i++){
        scanf("%ld", &arr[i]);
    }

    qsort(arr, N, sizeof(long), compare);

    int L = 0, R = N - 1;
    int answer = 0;

    while (L < R) {
        long temp = arr[L] + arr[R];
        if (temp == M) {
            answer += 1;
            L++, R--;
        }
        
        else if (temp < M){
            L++;
        }

        else{
            R--;
        }
    }

    printf("%d", answer);
}