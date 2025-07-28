l = int(input())
r = int(input())
total = 0
cnt = 2
while True:
    l = int(l * (r/100))
    if l <= 5:
        break
    total += (cnt * l)
    cnt *= 2
print(total)