# 12869

import sys
import math
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(math.ceil(int(input())/9))

else:
    arr = list(map(int, input().split()))
    arr.extend([0])
    possible_attack = [[9, 3, 1], [9, 1, 3], [
        3, 1, 9], [3, 9, 1], [1, 3, 9], [1, 9, 3]]

    dp = list(list([0]*61 for _ in range(61)) for _ in range(61))
    dp[arr[0]][arr[1]][arr[2]] = 1

    for i in range(60, -1, -1):
        for j in range(60, -1, -1):
            for k in range(60, -1, -1):
                if dp[i][j][k] > 0:
                    for p in possible_attack:
                        i1 = i-p[0] if i-p[0] >= 0 else 0
                        j1 = j-p[1] if j-p[1] >= 0 else 0
                        k1 = k-p[2] if k-p[2] >= 0 else 0
                        if dp[i1][j1][k1] == 0 or dp[i1][j1][k1] > dp[i][j][k] + 1:
                            dp[i1][j1][k1] = dp[i][j][k] + 1

    print(dp[0][0][0] - 1)
