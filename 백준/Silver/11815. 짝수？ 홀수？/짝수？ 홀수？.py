import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))

answer = list()

for i in arr:
    if i == 1:
        answer.append(1)
    elif int(i**(1/2))**2 != i:
        answer.append(0)
    else:
        answer.append(1)

print(*answer)