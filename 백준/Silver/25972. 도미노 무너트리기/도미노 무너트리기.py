import sys
input = sys.stdin.readline

n = int(input())
arr = list()

for _ in range(n):
    arr.append(list(map(int, input().split())))
    
arr.sort(key=lambda x:[x[0], x[1]])
answer = 0

for i in range(n):
    if i == 0:
        answer += 1
    else:
        if arr[i-1][0] + arr[i-1][1] >= arr[i][0]:
            continue
        else:
            answer += 1
            
print(answer)