# 12605

import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    temp = list(map(str, input().split()))
    temp.reverse()
    temp = ' '.join(temp)
    print(f'Case #{i}: ' + temp)
