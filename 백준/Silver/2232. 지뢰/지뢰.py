# 2232

import sys
input = sys.stdin.readline

arr = list()
mine = [0]
n = int(input())
for i in range(n):
    temp = int(input())
    mine.append(temp)
    arr.append((i+1, temp))

arr.sort(key=lambda x: -x[1])
arr.insert(0, (0, 0))

answer = list()

for i, j in arr:
    if mine[i] == 0:
        continue

    answer.append(i)
    if i == 1:
        i2 = i + 1
        right_shock = mine[i]
        while i2 <= n and mine[i2] < right_shock:
            right_shock = mine[i2]
            mine[i2] = 0
            i2 += 1

    elif i == n:
        i1 = i - 1
        left_shock = mine[i]
        while 1 <= i1 and mine[i1] < left_shock:
            left_shock = mine[i1]
            mine[i1] = 0
            i1 -= 1

    else:
        i1 = i - 1
        i2 = i + 1
        left_shock = mine[i]
        right_shock = mine[i]
        while 1 <= i1 and mine[i1] and mine[i1] < left_shock:
            left_shock = mine[i1]
            mine[i1] = 0
            i1 -= 1

        while i2 <= n and mine[i2] and mine[i2] < right_shock:
            right_shock = mine[i2]
            mine[i2] = 0
            i2 += 1

answer.sort()
for i in answer:
    print(i)
