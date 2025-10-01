//2493

#include <stdio.h>

#define MAX 500000

long N;
long arr[MAX];
long answer[MAX] = { 0 };
long stack[MAX] = { -1 };
long top = -1;

int main(void){
    scanf("%ld", &N);

    for (long i = 0; i < N; i++){
        scanf("%ld", &arr[i]);
    }


    for (long i = 0; i < N; i++) {
        while (top != -1 && arr[stack[top]] < arr[i]){
            stack[top--] = -1;
        }
        if (top == -1){
            stack[++top] = i;
        }
        else{
            answer[i] = stack[top] + 1;
            stack[++top] = i;
        }
        
    }

    for (long i = 0; i < N; i++) {
        printf("%ld ", answer[i]);
    }

    return 0;
}