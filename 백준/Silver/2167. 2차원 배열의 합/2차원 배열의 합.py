n,m = map(int, input().split())
arr = list()
arr.append(list(0 for _ in range(m+1)))
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))
    
for _ in range(int(input())):
    a,b,c,d=map(int, input().split())
    answer = 0
    
    for i in range(a, c+1):
        for j in range(b, d+1):
            answer += arr[i][j]
    
    print(answer)