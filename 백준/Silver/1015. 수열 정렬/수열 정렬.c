//1015

#include <stdio.h>

int n = 0;
int arr[50] = { 0, };

int main(void) {
    scanf("%d", &n);
    int frequency[1001] = { 0, };
    for (int i = 0; i < n; i++) {
        int temp;
        scanf("%d", &temp);
        arr[i] = temp;
        frequency[temp] += 1;
    }

    int answer[50];
    int answer_value = 0;

    for (int i = 1; i < 1001; i++){
        if (frequency[i] != 0) {
            for (int j = 0; j < 50; j++){
                if (arr[j] == i) {
                    answer[j] = answer_value;
                    answer_value += 1;
                }
            }
        }
    }

    for (int i = 0; i < n; i++){
        printf("%d ", answer[i]);
    }
}