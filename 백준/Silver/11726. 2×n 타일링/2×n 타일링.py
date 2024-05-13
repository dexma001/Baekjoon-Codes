# 11726

import sys
input = sys.stdin.readline

arr = list(0 for _ in range(1001))
arr[1] = 1
arr[2] = 2
for i in range(3, 1001):
    arr[i] = arr[i-1] + arr[i-2]

n = int(arr[int(input())])
print(n % 10007)
