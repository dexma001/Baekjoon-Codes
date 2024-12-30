a, b = map(int, input().split())
temp = max(a, b)
if temp % 2 == 0:
    print(0)
else:
    if min(a, b) % 2 == 0:
        print(0)
    else:
        print(min(a, b))
