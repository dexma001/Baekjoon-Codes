from collections import deque

n, m, r = map(int, input().split())

arr = list(list() for _ in range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
answer = list(-1 for _ in range(n+1))

temp = deque([])
temp.append(r)
answer[r] = 0

depth = 1
while temp:
    for i in range(len(temp)):
        t = temp.popleft()
        for j in arr[t]:
            if answer[j] == -1:
                answer[j] = depth
                temp.append(j)
    depth += 1
    
for i in range(1, n+1):
    print(answer[i])