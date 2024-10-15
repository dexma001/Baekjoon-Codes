# 1103

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(str, input().rstrip())))

dp = list(list(1 for _ in range(m)) for _ in range(n))
visited = list(list(0 for _ in range(m)) for _ in range(n))
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

visited[0][0] = 1
answer = 0


def dfs(i, j, k):
    global answer
    answer = max(answer, k)
    for t in range(4):
        y = i + dy[t] * int(arr[i][j])
        x = j + dx[t]*int(arr[i][j])

        if 0 <= y < n and 0 <= x < m and arr[y][x] != 'H' and k+1 > dp[y][x]:
            if visited[y][x]:
                print(-1)
                quit()
            else:
                dp[y][x] = k + 1
                visited[y][x] = 1
                dfs(y, x, k+1)
                visited[y][x] = 0


dfs(0, 0, 1)
print(answer)
'''
반례:
4 4
3HH2
H1HH
H2H1
2219

4 7
1HHHHH6
2H1HHHH
HH2H1HH
HHHH2H3

5 3
4HH
HHH
2H2
HHH
2H2
'''
