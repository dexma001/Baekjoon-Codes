//10610

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void make(char* n, int n_len, int* number_exist){
    int temp_sum = 0;

    for (int j = 0; j < n_len; j++) {
        if (n[j] != '0') {
            temp_sum += (n[j] - '0');
        }
    }

    if ((temp_sum % 3) != 0){
        printf("-1");
    } 

    else {
        int idx = 0;
        char* buffer;
        for (int k = 9; k > -1; k--){
            for (int l = 0; l < number_exist[k]; l++) {
                printf("%d", k);
            }
        }
    }

    return;
}

int main(void) {
    char n[100001];
    scanf("%s", n);
    char not_variable[2];


    int n_len = strlen(n);
    int number_exist[10];
    for (int i = 0; i < n_len; i++) {
        number_exist[n[i] - '0'] += 1;
    }

    if (number_exist[0] == 0){
        printf("%d", -1);
    }

    else {
        make(n, n_len, number_exist);
    }

    return 0;

}