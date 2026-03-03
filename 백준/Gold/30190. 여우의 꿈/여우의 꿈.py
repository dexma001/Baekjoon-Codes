#30190

import sys
input = sys.stdin.readline
INF = 10**9 + 7

n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

answer = 0

for i in range(n, 0, -1):
    if k == arr[i]:
        continue
    else:
        answer = (answer + pow(2, i-1, INF))%INF
        k = 6 - (k + arr[i])

print(answer)
