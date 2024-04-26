# 5525

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
string = str(input().rstrip())

answer = 0
left, right = 0, 0

while right < m:
    if string[right:right + 3] == 'IOI':
        right += 2

        if right - left == 2*n:
            answer += 1
            left += 2

    else:
        right += 1
        left = right

print(answer)
