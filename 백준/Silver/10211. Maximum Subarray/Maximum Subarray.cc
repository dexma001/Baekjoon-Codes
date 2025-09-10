// DP적 사고
// O(n^3) -> O(n^2) -> O(n)

#include <stdio.h>
#include <stdlib.h>

int function1(int *a, int n){
    int dp[100000];
    dp[0] = a[0];
    
    for (int j = 1; j < n; ++j) {
        if (dp[j-1] + a[j] < a[j]){
            dp[j] = a[j];
        }
        else {
            dp[j] = dp[j-1] + a[j];
        }
    }
    int temp = -1000001;
    for (int k = 0; k < n; ++k) {
        if (dp[k] > temp) {
            temp = dp[k];
        }
    }
    
    return temp;
}

int main(void) {
    int T;
    scanf("%d", &T);
    
    for (int p = 0 ; p < T; p++){
      int n;
      if (scanf("%d", &n) != 1 || n < 0) return 0;
      
      int a[100000];
      for (int i = 0; i < n; ++i){
        scanf("%d", &a[i]);
      } 
      
      printf("%d\n", function1(a, n));
    }
    return 0;
}