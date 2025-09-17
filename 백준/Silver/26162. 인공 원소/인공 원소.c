#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool is_artificial(const int* prime, int a){
    for (int left = 0; left < 118; left++){
        if (prime[left] == 0) {
            return false;
        }
        for (int right = 0; right <= left; right++){
            if (prime[left] + prime[right] == a){
                return true;
            }
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);

    int prime[118] = {0};
    int idx = 0;
    for (int i = 2; i <= 118; i++) {
        int judge = 0;
        for (int j = 2; j <= i / 2; j++) {
            if (judge == 1){
                break;
            }
            if (i % j == 0) {
                judge = 1;
            }
        }

        if(judge == 0) {
            prime[idx] = i;
            idx += 1;
        }
    }

    for (int i = 0; i < n; i++){
        int a;
        scanf("%d", &a);

        printf(is_artificial(prime, a) ? "Yes\n" : "No\n");
    }

    return 0;
}