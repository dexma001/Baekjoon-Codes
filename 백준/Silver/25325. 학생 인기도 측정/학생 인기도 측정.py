import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
a = list(map(str, input().split()))
arr = defaultdict(int)

for i in a:
    arr[i] = 0

for _ in range(n):
    temp = list(map(str, input().split()))
    for i in temp:
        arr[i] += 1

answer_arr = list(arr.items())
answer_arr.sort(key=lambda x:[-x[1], x[0]])

for i in answer_arr:
    print(*i)