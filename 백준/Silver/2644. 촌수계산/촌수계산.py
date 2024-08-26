# 2644

import sys
input = sys.stdin.readline

n = int(input())
ks1, ks2 = map(int, input().split())

arr = list([] for _ in range(n+1))

for _ in range(int(input())):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

answer = -1

visited = list(False for _ in range(n+1))
stack = list()
stack.append(ks1)
visited[ks1] = True
temp_answer = 1

while stack:
    for _ in range(len(stack)):
        temp = stack.pop(0)
        for i in arr[temp]:
            if i == ks2:
                answer = temp_answer
                break

            if not visited[i]:
                visited[i] = True
                stack.append(i)
    temp_answer += 1

print(answer)
