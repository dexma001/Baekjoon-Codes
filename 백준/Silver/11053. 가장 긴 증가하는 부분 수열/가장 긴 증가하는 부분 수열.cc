#include <stdio.h>
#include <stdlib.h>

int maximum_subarray_length(int *arr, int n){
    int *dp = (int*)malloc(sizeof(int)*(n > 0? n:1));
    
    for (int i = 0; i < n; i++){
      for (int j = i+1; j < n; j++){
        if (arr[i] < arr[j]){
          dp[j] = (dp[j] > dp[i] + 1 ? dp[j] : dp[i] + 1);
        }
      }
    }

    int temp_answer = 0;

    for (int k = 0; k < n; k++) {
      temp_answer = (temp_answer > dp[k] ? temp_answer : dp[k]);
    }

    free(dp);
    return temp_answer+1;
}

int main(void) {
    int n;
    scanf("%d", &n);

    int *arr = (int*)malloc(sizeof(int) * (n>0? n:1));
    for (int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    printf("%d\n", maximum_subarray_length(arr, n));
    free(arr);
    return 0;
}