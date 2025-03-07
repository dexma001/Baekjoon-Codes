n = int(input())
arr = list(map(int, input().split()))

answer = 0
temp = -1

for i in arr:
    if temp == -1:
        temp = i
        continue

    if i < temp:
        temp = i
    else:
        answer += 1
        temp = i

print(answer+1)
