# 9625

n = int(input())

a = 0
b = 1

for _ in range(n-1):
    c = a+b
    a = b
    b = c

print(a, b)
