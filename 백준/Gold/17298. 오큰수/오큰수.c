//17298

#include <stdio.h>

#define MAX 1000000

long N;
long arr[MAX];
long answer[MAX];

long stack[MAX];
long top = -1;

int main(void){
    scanf("%ld", &N);
    for (long i = 0; i < N; i++){
        scanf("%ld", &arr[i]);
        answer[i] = -1;
    }

    for (long i = 0; i < N; i++){
        while (top != -1 && arr[stack[top]] < arr[i]){
            answer[stack[top--]] = arr[i];
        }
        stack[++top] = i;
    }

    for (long i = 0; i < N; i++) {
        printf("%ld ", answer[i]);
    }
    return 0;
}