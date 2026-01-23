n = int(input())
arr = list(map(int, input().split()))

answer = 0

for i in range(n+1):
    if i == 0:
        answer += 1
    elif i == n:
        if arr[i] != 0:
            answer += len(str(arr[i])) + 1
    else:
        if arr[i] == 0:
            answer += 2
        else:
            answer += len(str(arr[i])) + 3

print(answer+1)