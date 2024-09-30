# 9576

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(0 for _ in range(n+1))
    stu = list()
    for _ in range(m):
        stu.append(list(map(int, input().split())))

    stu.sort(key=lambda x: [-x[0], x[1]])

    answer = 0
    for i, j in stu:
        for k in range(j, i-1, -1):
            if arr[k] == 0:
                answer += 1
                arr[k] = 1
                break

    print(answer)
