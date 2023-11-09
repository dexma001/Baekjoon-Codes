import sys
input = sys.stdin.readline
n, m = map(int, input().split())

li = [list(map(int, input().split())) for i in range(n)]
sum = [[0 for i in range(n+1)] for i in range(n+1)]

for i in range(n):
    for j in range(n):
        sum[i+1][j+1] = sum[i][j+1] + sum[i+1][j] - sum[i][j] + li[i][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1])
