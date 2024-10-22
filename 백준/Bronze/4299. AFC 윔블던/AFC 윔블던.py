n, m = map(int, input().split())
temp = (n+m)//2
k = n - temp

if (n+m) % 2 != 0 or n < m:
    print(-1)
else:
    print(max(temp, k), min(temp, k))
