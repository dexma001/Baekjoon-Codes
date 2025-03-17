import itertools

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
temp = list(itertools.combinations(arr, m))
for i in temp:
    print(*i)
