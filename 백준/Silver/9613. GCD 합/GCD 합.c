//9613

#include <stdio.h>
#include <stdlib.h>
int T;

long calculate(long i, long j) {
    if (j == 0){
        return i;
    }
    else{
        return calculate(j, i % j);
    }
}

long GCD(int N, long* arr) {
    long answer = 0;
    for (int i = 0; i < N - 1; i++){
        for (int j = i + 1; j < N; j++) {
            answer += calculate(arr[i], arr[j]);
        }
    }
    return answer;
}

int main(void) {
    scanf("%d\n", &T);
    for (int i = 0; i < T; i++) {
        int N;
        long arr[100];
        scanf("%d", &N);
        for (int j = 0; j < N; j++){
            scanf("%ld", &arr[j]);
        }
        printf("%ld\n", GCD(N, arr));
    }
}