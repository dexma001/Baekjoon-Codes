# 18111

import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())


arr = list()
for _ in range(n):
    temp = list(map(int, input().split()))
    arr.extend(temp)

height = max(arr)
land = min(arr)
s_block = sum(arr)

best = 500*500*2*257
best_fill = arr[0]

for fl in range(height, land-1, -1):
    if s_block + b >= fl*n*m:
        temp_time = 0
        for i in arr:
            dif = i - fl
            if dif > 0:
                temp_time += dif * 2
            elif dif < 0:
                temp_time += -dif

        if temp_time < best:
            best = temp_time
            best_fill = fl

print(best, best_fill)
