from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = set(map(int, input().split()))
arr = list(i for i in li)
arr.sort()

for i in combinations_with_replacement(arr, m):
    print(*i)
