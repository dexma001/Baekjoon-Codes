#include <stdio.h>
#include <math.h>
void recursion(int n){
    if (n == 0){
        printf("-");
        return;
    }

    if(n == 1){
        printf("%s", "- -");
        return;
    }

    recursion(n - 1);
    for (int i = 0; i < pow(3, n - 1); i++)
    {
        printf(" ");
    }
    recursion(n - 1);
    return;
}

int main(void){
    int n;
    while (scanf("%d", &n) != EOF){
        recursion(n);
        printf("\n");
    }
}