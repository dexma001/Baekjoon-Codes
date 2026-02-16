from collections import defaultdict

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    arr = defaultdict(int)

    for _ in range(n):
        arr[int(input())] = 1
        
    answer = 0

    for _ in range(m):
        temp = int(input())
        if arr[temp]:
            answer += 1

    print(answer)