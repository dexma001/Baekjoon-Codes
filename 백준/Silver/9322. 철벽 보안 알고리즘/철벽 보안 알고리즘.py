# 9322

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    open1 = list(map(str, input().split()))
    open2 = list(map(str, input().split()))
    code = list(map(str, input().split()))

    answer_arr = list()
    for i in range(n):
        answer_arr.append((i, open1.index(open2[i])))

    answer_arr.sort(key=lambda x: x[1])

    answer = list()
    for i in range(n):
        answer.append(code[answer_arr[i][0]])

    print(*answer)
