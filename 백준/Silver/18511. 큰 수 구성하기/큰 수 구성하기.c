#include <stdio.h>
#include <math.h>

long n;
long answer = 0;
void recursion(int* arr, int len, int loc, int temp_answer){
    if (n - temp_answer < 0){
        return;
    }

    if (temp_answer <= n && answer < temp_answer){
            answer = temp_answer;
    }

    for (int i = 0; i < len; i++){
        recursion(arr, len, loc + 1, temp_answer + (arr[i] * pow(10, loc)));
    }
    return;
}

int main(void){
    int k;
    scanf("%lld %d", &n, &k);

    int arr[3] = { 0 };
    for (int i = 0; i < k; i++){
        scanf("%d", &arr[i]);
    }
    recursion(arr, k, 0, 0);
    printf("%ld", answer);
    return 0;
}