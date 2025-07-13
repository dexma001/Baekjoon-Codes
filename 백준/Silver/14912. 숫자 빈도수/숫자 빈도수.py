n, d = map(int, input().split())
d = str(d)

answer = 0

for i in range(1, n+1):
    temp = list(p for p in str(i))
    for j in temp:
        if j == d:
            answer += 1
            
print(answer)