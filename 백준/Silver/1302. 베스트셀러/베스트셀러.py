# 1302

from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
arr = defaultdict(int)

for _ in range(n):
    temp = str(input().rstrip())
    arr[temp] -= 1

temp = list(arr.items())
temp.sort(key=lambda x: [x[1], x[0]])
print(temp[0][0])
