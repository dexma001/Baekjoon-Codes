#1120

import sys
input = sys.stdin.readline

a, b = map(str, input().split())
len_a = len(a)
len_b = len(b)

answer = 51

for i in range(len_b - len_a+1):
    temp_answer = 0
    for j in range(len_a):
        if a[j] != b[i+j]:
            temp_answer += 1
    answer = min(temp_answer, answer)

print(answer)