# 2352

import sys
import bisect
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))


answer = list()

for i in arr[1:]:
    if not answer or i > answer[-1]:
        answer.append(i)
    else:
        index = bisect.bisect_left(answer, i)
        answer[index] = i

print(len(answer))
