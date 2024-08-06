# 5052

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(input().rstrip() for _ in range(n))
    arr.sort()

    for i, j in zip(arr, arr[1:]):
        if j.startswith(i):
            print("NO")
            break
    else:
        print('YES')
