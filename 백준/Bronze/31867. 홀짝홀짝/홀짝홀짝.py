n = int(input())
temp = list(map(str, input().strip()))

odd = 0
even = 0

for i in temp:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

if odd > even:
    print(1)
elif odd < even:
    print(0)
else:
    print(-1)