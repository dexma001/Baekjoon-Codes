# 1051

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))

answer = 1

for i in range(n):
    for j in range(m):
        temp = 1
        while 0 <= i+temp < n and 0 <= j+temp < m:
            if arr[i][j] == arr[i][j+temp] == arr[i+temp][j] == arr[i+temp][j+temp]:
                answer = max(answer, (temp+1)**2)
            temp += 1

print(answer)
