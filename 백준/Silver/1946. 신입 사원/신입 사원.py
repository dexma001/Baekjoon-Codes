import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(0 for _ in range(n+1))
    
    for _ in range(n):
        a, b = map(int, input().split())
        arr[a] = b

    answer = 1
    temp = arr[1]
    for i in range(2, n+1):
        if arr[i] < temp:
            answer += 1
            temp = arr[i]
    
    print(answer)