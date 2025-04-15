# 10431

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    temp = list(map(int, input().split()))
    case = temp.pop(0)
    answer = 0
    for i in range(1, 20):
        for j in range(i):
            if temp[i] < temp[j]:
                answer += 1

    print(case, answer)
