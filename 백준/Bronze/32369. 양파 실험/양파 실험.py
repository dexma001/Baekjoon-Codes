n, a, b = map(int, input().split())

good, bad = 1, 1

for _ in range(n):
    good += a
    bad += b
    if bad > good:
        temp = bad
        bad = good
        good = temp

    elif good == bad:
        bad -= 1

print(good, bad)
