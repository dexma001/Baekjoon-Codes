temp = list(map(int, input().strip()))
leng = len(temp)
visited = list(0 for _ in range(leng))

answer = 0
for i in range(leng-2):
    if visited[i]:
        continue

    visited[i] = 1
    if temp[i+1]-temp[i] == 1 and temp[i+2]-temp[i+1] == 1:
        if i != leng-3:
            if temp[i+3]-temp[i+2] != 1:
                visited[i+1] = 1
                visited[i+2] = 1
                answer += 1
            else:
                while i < leng-1 and temp[i+1] - temp[i] == 1:
                    visited[i] = 1
                    i += 1
        else:
            visited[i+1] = 1
            visited[i+2] = 1
            answer += 1

print(answer)
