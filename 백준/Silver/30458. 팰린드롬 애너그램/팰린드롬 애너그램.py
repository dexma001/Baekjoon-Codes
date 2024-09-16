# 30458

from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(str, input().rstrip()))

temp = defaultdict(int)

for i in range(n//2):
    temp[arr[i]] += 1
    temp[arr[n-i-1]] += 1

for i in temp.keys():
    if temp[i] % 2 != 0:
        print('No')
        break
else:
    print('Yes')
