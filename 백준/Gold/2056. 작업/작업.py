# 2056

import sys
input = sys.stdin.readline

n = int(input())
time = [0] * (n+1)
previous = [[]] * (n+1)

for i in range(n):
    arr = list(map(int, input().split()))
    time[i+1] = arr[0]
    previous[i+1] = arr[2:]

edge = list([] for _ in range(n+1))
edge_in = list(0 for _ in range(n+1))

for i in range(1, n+1):
    for j in previous[i]:
        edge[j].append(i)
        edge[i].append(j)
        edge_in[i] += 1

visited = [False] * (n+1)
stack = list()
for i in range(1, n+1):
    if edge_in[i] == 0:
        stack.append(i)

dp = [0] * (n+1)
while stack:
    for _ in range(len(stack)):
        i = stack.pop(0)
        if visited[i] == True:
            continue
        visited[i] = True
        for k in previous[i]:
            dp[i] = max(dp[i], time[k])
        dp[i] += time[i]
        time[i] = dp[i]
        for j in edge[i]:
            if visited[j] == False:
                edge_in[j] -= 1
            if edge_in[j] == 0:
                stack.append(j)

print(max(dp))
