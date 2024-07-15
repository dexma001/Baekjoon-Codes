# 27648

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

if n + m-1 > k:
    print('NO')

else:
    print('YES')
    i = 1
    for _ in range(n):
        print(*list(k for k in range(i, i+m)))
        i += 1
