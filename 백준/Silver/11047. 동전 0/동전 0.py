# 11047

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
money_list = list()
answer = 0

for _ in range(n):
    money_list.append(int(input()))

money_list.reverse()

for i in money_list:
    if i > m:
        continue
    else:
        temp = m // i
        answer += temp
        m -= temp * i

        if m == 0:
            print(answer)
            break
