# 3944

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(str, input().split())
    k = 0
    for i in b:
        k += int(i)
    print(k % (int(a)-1))
