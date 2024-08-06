# 2776

from collections import defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))

    arr = defaultdict(int)
    for i in li:
        if arr[i] == 0:
            arr[i] = 1

    m = int(input())
    answer = list(map(int, input().split()))

    for j in answer:
        if arr[j]:
            print(1)
        else:
            print(0)
