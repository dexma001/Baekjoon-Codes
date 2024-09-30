# 1039

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
length = len(str(n))

if m > 5:
    if m % 2 == 0:
        m == 4
    else:
        m == 5

if length == 1:
    print(-1)
    quit()

arr = deque([])
arr.append(n)

for _ in range(m):
    tot = defaultdict(int)
    for _ in range(len(arr)):
        temp = str(arr.popleft())
        for i in range(length-1):
            for j in range(i+1, length):
                if i == 0 and temp[j] == '0':
                    continue
                ttemp = int(temp[0:i]+temp[j]+temp[i+1:j] +
                            temp[i]+temp[j+1:length])
                if not tot[ttemp]:
                    arr.append(ttemp)
                    tot[ttemp] = 1

if not arr:
    print(-1)
else:
    print(max(arr))
