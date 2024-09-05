# 1058

import sys
input = sys.stdin.readline

n = int(input())
arr = list()

for _ in range(n):
    arr.append(list(map(str, input().rstrip())))

answer = 0

for i in range(n):
    visited = list(0 for _ in range(n))
    visited[i] = 1
    temp_answer = 0

    for j in range(n):
        if arr[i][j] == 'Y':
            if not visited[j]:
                visited[j] = 1
                temp_answer += 1

            for k in range(n):
                if arr[j][k] == 'Y' and not visited[k]:
                    visited[k] = 1
                    temp_answer += 1

    answer = max(answer, temp_answer)

print(answer)
