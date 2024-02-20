# 2143 - 누적합

import sys
input = sys.stdin.readline


def perfixSum(x, arr1, arr2):
    for i in range(x):
        if i == 0:
            arr2[i+1] = arr1[i]
        else:
            arr2[i+1] = arr2[i] + arr1[i]
    return -1


t = int(input())
a = int(input())
a_arr = list(map(int, input().split()))
b = int(input())
b_arr = list(map(int, input().split()))

a_perfixSum = list([0] * (a+1))
b_perfixSum = list([0] * (b+1))

perfixSum(a, a_arr, a_perfixSum)
perfixSum(b, b_arr, b_perfixSum)

answer = 0
cnt_b_perfixSum = dict()

for x in range(b):
    for y in range(x, b):
        b_sum = b_perfixSum[y+1] - b_perfixSum[x]
        if b_sum in cnt_b_perfixSum.keys():
            cnt_b_perfixSum[b_sum] += 1
        else:
            cnt_b_perfixSum[b_sum] = 1

for i in range(a):
    for j in range(i, a):
        a_sum = a_perfixSum[j+1] - a_perfixSum[i]
        if (t - (a_sum)) in cnt_b_perfixSum.keys():
            answer += cnt_b_perfixSum[(t-(a_sum))]

print(answer)
