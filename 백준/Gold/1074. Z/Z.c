#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
long long answer = 0;

int Z(int r, int c, int K, long long answer) {
    if ((r/K)%2 == 1 & (c/K)%2 == 1) {
        answer += K * K * 3;
    }

    else if ((r/K)%2 == 1 & (c/K)%2 == 0) {
        answer += K * K * 2;
    }

    else if ((r/K)%2 == 0 & (c/K)%2 == 1) {
        answer += K * K;
    }
    
    if (K == 1) {
        printf("%lld", answer);
        return 0;
    }
    else {
        return Z(r, c, K/2, answer);
    }
}

int main(void) {
    int N, r, c;
    scanf("%d %d %d", &N, &r, &c);
    
    int K = pow(2, N-1);

    Z(r, c, K, answer);
    return 0;
}