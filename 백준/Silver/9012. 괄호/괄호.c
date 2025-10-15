#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_STACK_LEN 50

typedef struct{
    char stack[MAX_STACK_LEN];
    int top;
} StackType;

void init_stack(StackType* s){
    s->top = -1;
}

int is_empty(StackType* s){
    return (s->top == -1);
}

int is_full(StackType*s ){
    return (s->top == (MAX_STACK_LEN - 1));
}

void push(StackType*s, int value){
    s->stack[++s->top] = value;
}

void pop(StackType*s ){
    s->top--;
}

int main(void){
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        StackType s;
        init_stack(&s);
        int answer = 1;
        char string[MAX_STACK_LEN];
        scanf("%s", &string);
        int len = strlen(string);

        for (int j = 0; j < len; j++){
            char temp = string[j];

            if (temp == '(')
            {
                push(&s, temp);
            }
            else{
                if (is_empty(&s)) {
                    answer = 0;
                }

                else{
                    pop(&s);
                }
            }
        }

        if (!is_empty(&s)){
            answer = 0;
        }
        
        if (answer == 1){
            printf("YES\n");
        }
        else{
            printf("NO\n");
        }
    }
    return 0;
}