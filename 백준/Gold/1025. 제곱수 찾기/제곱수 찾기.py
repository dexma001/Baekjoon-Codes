import sys
import numbers
import math

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(str, sys.stdin.readline().strip())))
answer = -1


def inte(z):
    z = int(z)
    return int(z**0.5)**2 == z


for i in range(n):
    for j in range(m):
        for AS_n in range(-n, n):
            for AS_m in range(-m, m):
                s = ""
                x, y = i, j
                if AS_n == 0 and AS_m == 0:
                    continue
                while 0 <= x < n and 0 <= y < m:
                    s += arr[x][y]
                    if inte(s) == True:
                        answer = max(answer, int(s))
                    x += AS_n
                    y += AS_m

print(answer)
