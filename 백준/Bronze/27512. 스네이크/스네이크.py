n, m = map(int, input().split())
if n % 2 != 0 and m % 2 != 0:
    print(n*m-1)
else:
    print(n*m)