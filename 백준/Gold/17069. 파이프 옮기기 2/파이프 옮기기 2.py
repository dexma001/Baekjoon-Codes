# 17070

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
li = list()
answer = 0

for _ in range(n):
    li.append(list(map(int, input().split())))

dp_arr = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
# 가 / 세 / 대
dp_arr[0][1][0] += 1

for x in range(1, n):
    if li[0][x] != 1:
        dp_arr[0][x][0] += dp_arr[0][x-1][0]

for i in range(1, n):
    for j in range(1, n):
        if li[i][j] != 1:
            if li[i-1][j] & li[i][j-1] == 1:
                continue
            elif li[i-1][j] == 0 and li[i][j-1] == 1:
                dp_arr[i][j][1] = dp_arr[i-1][j][1] + dp_arr[i-1][j][2]
            elif li[i-1][j] == 1 and li[i][j-1] == 0:
                dp_arr[i][j][0] = dp_arr[i][j-1][0] + dp_arr[i][j-1][2]
            else:
                dp_arr[i][j][2] = dp_arr[i-1][j-1][0] + \
                    dp_arr[i-1][j-1][1] + dp_arr[i-1][j-1][2]
                dp_arr[i][j][0] = dp_arr[i][j-1][0] + dp_arr[i][j-1][2]
                dp_arr[i][j][1] = dp_arr[i-1][j][1] + dp_arr[i-1][j][2]


print(dp_arr[n-1][n-1][0] + dp_arr[n-1][n-1][1] + dp_arr[n-1][n-1][2])
