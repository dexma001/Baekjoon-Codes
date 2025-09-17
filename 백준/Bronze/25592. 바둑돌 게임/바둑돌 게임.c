#include <stdio.h>
#include <stdlib.h>

int main(void) {
    long N;
    scanf("%ld", &N);

    int answer = 0;
    int count = 1;

    while (1) {
        if (N < count){
            answer = (count - N);
            break;
        }

        N -= count++;

        if (N < count) {
            break;
        }
        else{
            N -= count++;
        }
    }

    printf("%d", answer);
    return 0;
}