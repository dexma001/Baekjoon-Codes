# 1238

import sys
input = sys.stdin.readline

cnt_city, cnt_road, party = map(int, input().split())
arr = list(list(1000001 for _ in range(cnt_city))
           for _ in range(cnt_city))
dis = 0

for i in range(cnt_road):
    n, m, l = map(int, input().split())
    arr[n-1][m-1] = l

for k in range(cnt_city):
    for i in range(cnt_city):
        if arr[i][k] != 1000001:
            for j in range(cnt_city):
                if i == j:
                    arr[i][j] = 0
                else:
                    arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

for u in range(cnt_city):
    dis = max(dis, arr[u][party-1] + arr[party-1][u])

print(dis)
