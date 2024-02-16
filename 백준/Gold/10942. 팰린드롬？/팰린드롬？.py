# 10942

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
palin_db = list(list([0])*n for _ in range(n))

for i in range(n):
    for j in range(0, n-i):
        if i == 0:
            palin_db[j][j+i] = 1
        elif i == 1:
            if num_list[j] != num_list[j+i]:
                palin_db[j][j+i] = 0
            else:
                palin_db[j][j+i] = 1
        else:
            if num_list[j] != num_list[j+i]:
                palin_db[j][j+i] = 0
            else:
                palin_db[j][j+i] = palin_db[j+1][j+i-1]

m = int(input())
for _ in range(m):
    start, end = map(int, input().split())
    print(palin_db[start-1][end-1])
