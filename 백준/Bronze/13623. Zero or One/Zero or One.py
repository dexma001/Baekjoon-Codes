#13623

import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
abc = ['A', 'B', 'C']

if arr.count(0) == 1:
    print(abc[arr.index(0)])
elif arr.count(0) == 2:
    print(abc[arr.index(1)])
else:
    print('*')