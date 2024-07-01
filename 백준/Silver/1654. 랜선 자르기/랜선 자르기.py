# 1654

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()

for _ in range(n):
    arr.append(int(input()))

temp = max(arr)

answer = 0


def binary_search(start, end):
    global answer
    if start > end:
        return

    middle = (start+end)//2
    temp_answer = 0
    for i in arr:
        temp_answer += (i//middle)

    if temp_answer >= m:
        answer = max(answer, middle)
        start = middle + 1
    else:
        end = middle - 1

    return binary_search(start, end)


binary_search(1, temp)
print(answer)
