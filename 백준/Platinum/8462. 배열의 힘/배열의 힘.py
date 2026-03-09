#8462

import sys
input = sys.stdin.readline
import math
from collections import deque

n, t = map(int, input().split())
arr = [0] + list(map(int, input().split()))

answer = list()
for i in range(t):
    l, r = map(int, input().split())
    answer.append([i, l, r, 0, l//math.sqrt(n)]) #index, left, right, answer, mo's

answer.sort(key=lambda x:[x[4], x[2]])

left = answer[0][1]
right = answer[0][1] - 1
pow = 0
cnt = list(0 for _ in range(1000001))

def add(val):
    global pow
    if cnt[val] != 0:
        pow -= cnt[val] * cnt[val] * val
    cnt[val] += 1
    pow += cnt[val] * cnt[val] * val
    
def remove(val):
    global pow

    pow -= cnt[val] * cnt[val] * val
    cnt[val] -= 1
    pow += cnt[val] * cnt[val] * val

for i in range(t):
    while left > answer[i][1]:
        left -= 1
        add(arr[left])

    while right < answer[i][2]:
        right += 1
        add(arr[right])

    while left < answer[i][1]:
        remove(arr[left])
        left += 1

    while right > answer[i][2]:
        remove(arr[right])
        right -= 1

    answer[i][3] = pow

answer.sort(key=lambda x:[x[0]])

for i in answer:
    print(i[3])