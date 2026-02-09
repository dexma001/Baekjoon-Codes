from collections import deque

n, b, a = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = 0

answer = 0

for _ in range(a):
    if answer + arr[end] //2 > b:
        print(end)
        quit()
    
    else:
        answer += arr[end]//2
        end += 1
  
for _ in range(a, n):
    if answer + arr[start]//2 + arr[end]//2 <= b:
        answer += arr[start]//2
        answer += arr[end]//2
        start += 1
        end += 1
    else:
        print(end)
        break
    
else:
    print(end)