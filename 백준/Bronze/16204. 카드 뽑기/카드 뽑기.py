n, m, k = map(int, input().split())
print(min(n-m, n-k) + min(m, k))