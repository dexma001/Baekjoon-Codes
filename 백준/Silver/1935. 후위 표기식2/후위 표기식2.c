//1935

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int n;
    int alpha[26];
    char arr[100];

    scanf("%d\n", &n);
    scanf("%s", &arr);
    for (int i = 0; i < n; i++){
        scanf("%d", &alpha[i]);
    }

    char pmmd[4] = { '+', '-', '*', '/' };
    double answer[100] = { 0, };
    int answer_index = -1;
    for (int i = 0; i < 100; i++){
        if (!arr[i]) {
            break;
        }

        if (0<=(arr[i] - 'A') && (arr[i] - 'A') <=25) {
            answer[++answer_index] = (double)alpha[arr[i] - 'A'];
        }
        else{
            double second = answer[answer_index];
            answer[answer_index--] = 0;
            double first = answer[answer_index];
            answer[answer_index--] = 0;
            double temp = 0;
            for (int j = 0; j < 4; j++){
                if (arr[i] == pmmd[j]){
                    switch (pmmd[j]) {
                        case '+': temp = first + second; break;
                        case '-': temp = first - second; break;
                        case '*': temp = first * second; break;
                        case '/': temp = first / second; break;
                    }
                }
            }
            answer[++answer_index] = temp;
        }
    }
    printf("%.2f", answer[0]);
    return 0;
}