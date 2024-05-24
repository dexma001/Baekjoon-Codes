# 1495

import sys
from collections import defaultdict
input = sys.stdin.readline

n, s, m = map(int, input().split())
temp_arr = [0] + list(map(int, input().split()))


temp_dict = defaultdict(set)
temp_dict[0].add(s)

for i in range(1, n+1):
    for j in range(len(temp_dict[i-1])):
        if 0 <= list(temp_dict[i-1])[j] + temp_arr[i] <= m:
            temp_dict[i].add(list(temp_dict[i-1])[j] + temp_arr[i])
        if 0 <= list(temp_dict[i-1])[j] - temp_arr[i] <= m:
            temp_dict[i].add(list(temp_dict[i-1])[j] - temp_arr[i])

if len(temp_dict[n]) == 0:
    print(-1)
else:
    print(max(temp_dict[n]))
