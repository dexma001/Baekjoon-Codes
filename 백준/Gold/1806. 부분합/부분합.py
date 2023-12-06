# 1806

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

arr = deque([])
answer = 0

for i in range(n):
    arr.append(li[i])
    answer += li[i]
    if answer >= m:
        break
    else:
        if i == n-1:
            arr.clear()
            break
        else:
            continue

ans = len(arr)
a = ans - 1

if ans == 0:
    print(ans)
else:
    while True:
        num = arr.popleft()
        answer -= num
        if answer >= m:
            ans -= 1
            continue
        else:
            a = a + 1
            if a >= n:
                break
            else:
                arr.append(li[a])
                answer += li[a]
                continue
    print(ans)
