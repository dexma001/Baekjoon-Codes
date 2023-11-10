import sys
from itertools import permutations

n, m = map(int, input().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

ans = list(permutations(li, m))

for i in range(len(ans)):
    print(*ans[i])
