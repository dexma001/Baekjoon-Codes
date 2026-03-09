#14897

import sys
import math
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
ar = list(map(int, input().split()))

dic = {v: i for i, v in enumerate(sorted(set(ar)))}
arr = [0] + [dic[v] for v in ar]

answer_list = list()
q = int(input())

abc = math.sqrt(n)
for i in range(q):
    l, r = map(int, input().split())
    answer_list.append([i, l, r, 0, l//abc])

answer_list.sort(key=lambda x:(x[4], x[2]))

number = [0] * (len(dic)+1)
ans = 0
left = answer_list[0][1]
right = answer_list[0][1] - 1

for i in range(q):
    l = answer_list[i][1]
    r = answer_list[i][2]

    while left > l:
        left -= 1
        t = arr[left]
        if number[t] == 0:
            number[t] += 1
            ans += 1
        else:
            number[t] += 1
    while right < r:
        right += 1
        t = arr[right]
        if number[t] == 0:
            number[t] += 1
            ans += 1
        else:
            number[t] += 1
    while left < l:
        t = arr[left]
        number[t] -= 1
        if number[t] == 0:
            ans -=1
        left += 1
    while right > r:
        t = arr[right]
        number[t] -= 1
        if number[t] == 0:
            ans -= 1
        right -= 1

    answer_list[i][3] = ans

answer_list.sort(key=lambda x:(x[0]))

for i in answer_list:
    sys.stdout.write(f"{i[3]}\n")
