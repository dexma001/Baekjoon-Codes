import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n = int(input())
arr = deque([])
checking = defaultdict(int)
answer = 0
ans_check = 0

arr.append(n)
checking[n] = 1

while True:
    if ans_check:
        break
    for i in range(len(arr)):
        temp = arr.popleft()
        if temp == 1 or ans_check == 1:
            ans_check = 1
            break
        
        if temp % 3 == 0 and not checking[temp//3]:
            checking[temp//3] = 1
            arr.append(temp//3)
        if temp % 2 == 0 and not checking[temp//2]:
            checking[temp//2] = 1
            arr.append(temp//2)
        if not checking[temp-1]:
            checking[temp-1] = 1
            arr.append(temp-1)
    else:
        answer += 1

print(answer)