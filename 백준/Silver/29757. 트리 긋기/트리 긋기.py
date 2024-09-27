# 29757

import sys
input = sys.stdin.readline

n = int(input())
arr = list([list(map(int, input().split())), i+1] for i in range(n))

arr.sort(key=lambda x: [x[0][0], x[0][1]])

for i in range(n-1):
    print(arr[i][1], arr[i+1][1])
