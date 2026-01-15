n, m, q = map(int, input().split())
arr = list(list(0 for _ in range(m+1)) for _ in range(n+1))
score = list([i, 0, 0] for i in range(n+1))

for _ in range(q):
    temp = list(map(str, input().split()))
    for i in range(3):
        temp[i] = int(temp[i])
        
    if temp[-1] == 'AC':
        if arr[temp[1]][temp[2]] == -1:
            continue
        
        score[temp[1]][1] += 1
        score[temp[1]][2] += arr[temp[1]][temp[2]] * 20 + temp[0]
        arr[temp[1]][temp[2]] = -1
    
    else:
        if arr[temp[1]][temp[2]] == -1:
            continue
        
        arr[temp[1]][temp[2]] += 1
        
score.pop(0)
score.sort(key=lambda x:[-x[1], x[2], x[0]])

for i in score:
    print(*i)