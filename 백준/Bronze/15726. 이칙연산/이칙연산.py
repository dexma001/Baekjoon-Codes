import math

n, m, k = map(int, input().split())
print(max(math.floor(n*m/k), math.floor(n/m*k)))
