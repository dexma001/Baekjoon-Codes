# 9489

from collections import defaultdict
import sys
input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    if n == 0:
        break

    arr = list(map(int, input().split()))
    parent = defaultdict(int)

    temp = 0
    for i in range(1, n):
        parent[arr[i]] = arr[temp]
        if i < n-1 and arr[i]+1 < arr[i+1]:
            temp += 1

    answer = 0
    if parent[parent[k]]:
        for i in arr:
            if parent[i] != parent[k] and parent[parent[k]] == parent[parent[i]]:
                answer += 1

    print(answer)
