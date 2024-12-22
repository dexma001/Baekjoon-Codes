a, b, c = map(int, input().split())
time = int(input())

c += time

if c > 59:
    b += (c // 60)
    c = c % 60
    if b > 59:
        a += (b // 60)
        b = b % 60
        if a > 23:
            a = a % 24

print(a, b, c)
