# 1700

from collections import defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

how_many = defaultdict(int)
for i in arr:
    how_many[i] += 1

temp = list()
answer = 0

while arr and len(temp) < n:
    k = arr.pop(0)
    if k not in temp:
        temp.append(k)
        how_many[k] -= 1
    else:
        how_many[k] -= 1

while arr:
    i = arr.pop(0)
    if i in temp:
        how_many[i] -= 1
        continue
    else:
        for ii in temp:
            if how_many[ii] == 0:
                temp.remove(ii)
                temp.append(i)
                answer += 1
                how_many[i] -= 1
                break
        else:
            le = 0
            target = 0
            for ii in temp:
                for j in range(len(arr)):
                    if arr[j] == ii:
                        if j > le:
                            le = j
                            target = ii
                        break
            if le != 0:
                temp.remove(target)
                temp.append(i)
                answer += 1
                how_many[i] -= 1
            else:
                temp.pop(0)
                temp.append(i)
                answer += 1
                how_many[i] -= 1
print(answer)
