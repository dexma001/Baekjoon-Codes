# 6764

from copy import deepcopy
import sys
input = sys.stdin.readline


arr = list()
for _ in range(4):
    arr.append(int(input()))

arr_upper = list(set(deepcopy(arr)))
arr_lower = list(set(deepcopy(arr)))
is_constant = set(deepcopy(arr))

arr_upper.sort()
arr_lower.sort(reverse=True)

if len(is_constant) == 1:
    print('Fish At Constant Depth')

elif arr == arr_upper:
    print('Fish Rising')

elif arr == arr_lower:
    print('Fish Diving')

else:
    print('No Fish')
