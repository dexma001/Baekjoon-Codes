import math

r, c, n = map(int, input().split())

a = math.ceil(r/n)
b = math.ceil(c/n)
print(a*b)
