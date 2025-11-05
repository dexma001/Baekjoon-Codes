#30389

import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
arr = defaultdict(int)

for _ in range(n):
    string = str(input())
    string_len = len(string)

    for i in range(string_len-2, -1, -1):
        arr[string[i:-1]] += 1

answer = 0

temp = list(arr.items())
for i, j in temp:
    if j %2 != 0:
        answer +=1

print(answer)