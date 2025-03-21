import itertools

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

temp = list(itertools.product(arr, repeat=m))
for i in temp:
    print(*i)
