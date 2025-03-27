# 5585

import sys
input = sys.stdin.readline

arr = 1000 - int(input())
answer = 0

temp = [500, 100, 50, 10, 5, 1]

for i in temp:
    answer += arr//i
    arr %= i

print(answer)
