# 1522

import sys
input = sys.stdin.readline

temp = str(input().rstrip())
a_count = temp.count('a')

temp += temp[0:a_count-1]

answer = 10**9
for i in range(0, len(temp)-(a_count-1)):
    answer = min(answer, temp[i:i+a_count].count('b'))

print(answer)
