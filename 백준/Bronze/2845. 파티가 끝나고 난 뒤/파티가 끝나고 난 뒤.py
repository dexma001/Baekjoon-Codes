n, m = map(int, input().split())
tot = n*m
arr = list(map(int, input().split()))
for i in arr:
    print(i - tot)