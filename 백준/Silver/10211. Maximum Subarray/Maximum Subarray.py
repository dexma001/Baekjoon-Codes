# 10211

import sys
input = sys.stdin.readline

case = int(input())

for _ in range(case):
    temp = int(input())
    arr = [0] + list(map(int, input().split()))

    answer = arr[1]
    for i in range(1, temp+1):
        temp_answer = arr[i]
        answer = max(answer, temp_answer)
        for j in range(i+1, temp+1):
            temp_answer += arr[j]
            answer = max(answer, temp_answer)

    print(answer)
