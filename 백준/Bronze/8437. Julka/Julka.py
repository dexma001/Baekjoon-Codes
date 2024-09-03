n = int(input())
m = int(input())

if n % 2 == 0:
    print(n//2 + m//2)
    print(n//2 - m//2)
else:
    print(n - (n//2 - m//2))
    print(n//2 - m//2)
