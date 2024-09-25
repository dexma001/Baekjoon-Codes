# 3863

import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 or m == 0:
        break

    arr = list()

    for _ in range(n):
        temp = list(map(int, input().split()))
        arr.append([temp[2], temp[2]+temp[3]])

    for _ in range(m):
        p, q = map(int, input().split())
        answer = 0
        for i, j in arr:
            if i >= p+q or j <= p:
                continue
            answer += 1
        print(answer)
