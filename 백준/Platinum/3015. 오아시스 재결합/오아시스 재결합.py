# 3015 - 오아시스 재결합

import sys
input = sys.stdin.readline

n = int(input())
people = list()
same_len = dict()
for _ in range(n):
    a = int(input())
    people.append(a)
    same_len[a] = 1

answer = 0
stack = list()

i = 0
while i < n:
    if len(stack) == 0:
        stack.append(people[i])
        i += 1
    else:
        if people[i] < stack[-1]:
            answer += 1
            stack.append(people[i])
            i += 1
        elif people[i] == stack[-1]:
            answer += same_len[stack[-1]]
            same_len[stack[-1]] += 1
            stack.pop()
        else:
            answer += same_len[stack[-1]]
            same_len[stack[-1]] = 1
            stack.pop()

print(answer)
