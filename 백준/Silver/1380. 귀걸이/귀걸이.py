# 1380

import sys
input = sys.stdin.readline

k = 1
while True:
    n = int(input())
    if n == 0:
        break
    student = ['']
    for _ in range(n):
        student.append(str(input().strip()))
    temp = list()
    for _ in range(2*n-1):
        a, b = map(str, input().split())
        if a in temp:
            temp.remove(a)
        else:
            temp.append(a)
    print(k, student[int(temp[0])])
    k += 1
