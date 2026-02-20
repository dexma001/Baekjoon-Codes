from collections import deque

n = int(input())

arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = 0
temp = deque([])
temp.append([0, 0])

visited = list(list(0 for _ in range(n)) for _ in range(n))
visited[0][0] = 1

while temp:
    if answer:
        break
    
    for _ in range(len(temp)):
        a, b = temp.popleft()
        if a == n-1 and b == n-1:
            answer = 1
            break
        
        if a + arr[a][b] < n and not visited[a+arr[a][b]][b]:
            visited[a+arr[a][b]][b] = 1
            temp.append([a+arr[a][b], b])
            
        if a - arr[a][b] >= 0 and not visited[a-arr[a][b]][b]:
            visited[a-arr[a][b]][b] = 1
            temp.append([a-arr[a][b], b])
            
        if b + arr[a][b] < n and not visited[a][b+arr[a][b]]:
            visited[a][b+arr[a][b]] = 1
            temp.append([a, b+arr[a][b]])
            
        if b - arr[a][b] >= 0  and not visited[a][b-arr[a][b]]:
            visited[a][b-arr[a][b]] = 1
            temp.append([a, b-arr[a][b]])

if answer:
    print("HaruHaru")
else:
    print("Hing")