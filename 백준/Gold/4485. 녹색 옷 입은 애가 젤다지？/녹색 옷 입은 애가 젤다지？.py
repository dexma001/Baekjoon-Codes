#4485

import sys
input = sys.stdin.readline
from collections import deque

case = 1
while True:
    n = int(input())
    if n == 0:
        break
    
    arr = list()
    for _ in range(n):
        arr.append(list(map(int, input().split())))
        
    dp = list(list(-1 for _ in range(n)) for _ in range(n))

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    stack = deque([])
    dp[0][0] = arr[0][0]
    stack.append([0, 0, dp[0][0]])
    
    while stack:
        p,q,r= stack.popleft()
        for i in range(4):
            y = p + dy[i]
            x = q + dx[i]
            if 0<=y<n and 0<=x<n:
                if dp[y][x] == -1:
                    dp[y][x] = r + arr[y][x]
                    stack.append([y, x, dp[y][x]])
                else:
                    if r + arr[y][x] < dp[y][x]:
                        dp[y][x] = r + arr[y][x]
                        stack.append([y, x, dp[y][x]])

    print(f"Problem {case}: {dp[-1][-1]}")
    case += 1