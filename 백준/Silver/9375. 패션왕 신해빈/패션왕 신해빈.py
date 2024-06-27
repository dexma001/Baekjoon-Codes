# 9375

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    temp = dict()
    len_dict = 0

    for _ in range(n):
        a, b = input().split()
        try:
            if temp[b]:
                temp[b] += 1
        except:
            temp[b] = 1
            len_dict += 1

    answer = 1
    for a in temp.values():
        answer *= (a + 1)
    print(answer-1)
