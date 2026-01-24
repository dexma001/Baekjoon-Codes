import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = defaultdict(int)
for i in arr:
    cnt[i] += 1
    
cnt_list = list(cnt.items())
cnt_list.sort(key=lambda x:[-x[1], -x[0]])

answer = 0
for i, j in cnt_list:
    answer = max(answer, i*j)
    
print(sum(arr) + answer)
print(*arr)