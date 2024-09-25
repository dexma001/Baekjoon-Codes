# 12034

import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    answer = list()

    while arr:
        i = arr.pop(0)
        answer.append(str((i//4)*3))
        arr.remove((i//4)*3)

    answer.reverse()

    print(f"Case #{t+1}: {' '.join(i for i in answer)}")
