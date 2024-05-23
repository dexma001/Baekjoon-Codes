# 13301

n = int(input())
if n == 1:
    print(4)
elif n == 2:
    print(6)
else:
    a = 4
    b = 6
    for _ in range(n-2):
        c = a+b
        a = b
        b = c
    print(b)
