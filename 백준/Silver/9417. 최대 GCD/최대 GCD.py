import math

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    answer = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            answer = max(answer, math.gcd(arr[i], arr[j]))
    print(answer)
