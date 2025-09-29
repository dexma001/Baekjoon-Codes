#include <stdio.h>
#include <string.h>

int main(void){
    while (1) {
        int n = 0;
        int m = 0;
        scanf("%d %d", &n, &m);
        if (n == 0 || m == 0){
            break;
        }
        int answer = 0;
        for (int i = n; i <= m; i++){
            char result[5];
            sprintf(result, "%d", i);
            int dup[10] = { 0, };
            int temp_answer = 0;
            int len = strlen(result);
            if (len) {
                for (int j = 0; j < len; j++) {
                    int digit = result[j] - '0';
                    if (dup[digit]) {
                        temp_answer = 1;
                        break;
                    }
                    dup[digit] = 1;
                }
                if (temp_answer == 0){
                    answer += 1;
                }
            }   
        }
        printf("%d\n", answer);
    }

    return 0;
}