import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list()

for _ in range(n):
    arr.append(int(input()))
    
temp = 0
answer = 0

for i in range(151):
    if temp == k:
        break
    temp = arr[temp]
    answer += 1
    
if answer == 151:
    print(-1)
else:
    print(answer)
    