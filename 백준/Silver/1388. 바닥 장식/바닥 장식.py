n, m = map(int, input().split())

arr = list()
for _ in range(n):
    arr.append(list(map(str, input().strip())))
    
answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '-1':
            continue
        
        elif arr[i][j] == '-':
            arr[i][j] = '-1'
            if j == m-1:
                answer += 1
            else:
                t = 1
                while j+t < m and arr[i][j+t] == '-':
                    arr[i][j+t] = '-1'
                    t += 1
                answer += 1
        else:
            arr[i][j] == '-1'
            if i == n-1:
                answer += 1
            else:
                t = 1
                while i + t < n and arr[i+t][j] == '|':
                    arr[i+t][j] = '-1'
                    t += 1
                answer += 1

print(answer)