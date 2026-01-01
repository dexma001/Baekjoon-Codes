import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**9)


arr = list()
for _ in range(5):
    arr.append(list(map(str, input().split())))
    
visited = defaultdict(int)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def dfs(i, j, number, length):
    if length == 6:
        if not visited[number]:
            visited[number] = 1
        return
    
    for p in range(4):
        y = i + dy[p]
        x = j + dx[p]
        if 0<=y<5 and 0<=x<5:
            dfs(y, x, number+arr[y][x], length+1)

for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j], 1)
        
print(len(list(visited.keys())))