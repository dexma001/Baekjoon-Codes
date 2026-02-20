from collections import deque

n, m = map(int, input().split())
arr = list()
for _ in range(m):
    arr.append(list(map(int, input().split())))
    
temp = deque([])
temp.append([0, 0])
arr[0][0] = -1

dy = [1, 0]
dx = [0, 1]

answer = 0
while temp:
    if answer:
        break
    
    for _ in range(len(temp)):
        a, b = temp.popleft()
        if a == m-1 and b == n-1:
            answer = 1
            break
        for i in range(2):
            y = a + dy[i]
            x = b + dx[i]
            if 0<=y<m and 0<=x<n and arr[y][x] == 1:
                arr[y][x] = -1
                temp.append([y, x])

print("Yes") if answer else print("No")