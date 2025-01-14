# 1497

import sys
input = sys.stdin.readline

n = int(input())
cls = list()
for _ in range(n):
    arr = list(map(int, input().split()))[1:]
    temp = 0
    for i in arr:
        temp |= 1 << (i-1)
    cls.append(temp)

m = int(input())
for _ in range(m):
    stu = list(map(int, input().split()))[1:]
    temp = 0
    for i in stu:
        temp |= 1 << (i-1)

    answer = 0
    for j in cls:
        if temp | j == temp:
            answer += 1

    print(answer)
