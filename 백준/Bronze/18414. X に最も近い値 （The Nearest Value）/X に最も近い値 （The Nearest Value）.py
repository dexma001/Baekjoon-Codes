n,l,r = map(int, input().split())

if n > r:
    print(r)
elif n < l:
    print(l)
else:
    print(n)