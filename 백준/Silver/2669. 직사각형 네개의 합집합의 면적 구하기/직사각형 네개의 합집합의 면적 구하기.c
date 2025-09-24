#include <stdio.h>

int a, b, c, d;

int main(void) {
    int arr[101][101] = { 0, };

    for (int i = 0; i < 4; i++) {
        scanf("%d %d %d %d\n", &a, &b, &c, &d);
        for (int x = a; x < c; x++){
            for (int y = b; y < d; y++){
                arr[y][x] = 1;
            }
        }
    }

    int answer = 0;
    for (int i = 1; i <= 100; i++) {
        for (int j = 1; j <= 100; j++) {
            if (arr[i][j] == 1) {
                answer += 1;
            }
        }
    }

    printf("%d", answer);
    return 0;
}