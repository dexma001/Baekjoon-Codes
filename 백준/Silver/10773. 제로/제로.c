//10773

#include <stdio.h>

#define MAX 100000

typedef struct {
    long a[MAX];
    long top;
} Stack;

void push(Stack* s, int v){
    s->a[++s->top] = v;
}

int pop(Stack* s){
    return s->a[s->top--];
}

int main(void) {
    long K;
    scanf("%ld", &K);
    Stack list;
    list.top = -1;

    for (long i = 0; i < K; i++){
        long temp;
        scanf("%ld", &temp);
        if (temp == 0){
            pop(&list);
        }
        else {
            push(&list, temp);
        }
    }

    long answer = 0;
    for (long i = 0; i <= list.top; i++) {
        answer += list.a[i];
    }

    printf("%ld", answer);
    return 0;
}