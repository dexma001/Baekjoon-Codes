import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))

answer = list()

for i in arr:
    if i == 1 or int(i**(1/2))**2 == i:
        answer.append(1) 
    else:
        answer.append(0)

print(*answer)