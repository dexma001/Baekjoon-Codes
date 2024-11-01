n, m = map(int, input().split())
k = int(input())
if n+m >= 2*k:
    print(n+m-(2*k))
else:
    print(n+m)