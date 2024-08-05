# 9933

import sys
input = sys.stdin.readline

n = int(input())
arr = list()

answer = ''
for _ in range(n):
    temp = str(input().rstrip())
    if temp == temp[::-1]:
        answer = temp

    else:
        for k in arr:
            if temp == k[::-1]:
                answer = temp

    arr.append(temp)

print(len(answer), answer[len(answer)//2])
