from itertools import combinations

n, m = map(int, input().split())

li = [i+1 for i in range(n)]

for i in combinations(li, m):
    print(*i)
