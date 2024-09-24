# 3077

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(str, input().split()))
ques = dict()
for i in range(n):
    ques[arr[i]] = i + 1

answer = 0
temp = list(map(str, input().split()))
for i in range(n):
    for j in range(i, n):
        if ques[temp[i]] < ques[temp[j]]:
            answer += 1

print(f"{answer}/{n*(n-1)//2}")
