# 25601

from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
arr = defaultdict()

for _ in range(n-1):
    a, b = map(str, input().split())
    arr[a] = b

n, m = map(str, input().split())


def dfs(tree, a, b):
    while True:
        try:
            a = tree[a]
            if a == b:
                return True
        except:
            return False


if dfs(arr, n, m) or dfs(arr, m, n):
    print(1)
else:
    print(0)
