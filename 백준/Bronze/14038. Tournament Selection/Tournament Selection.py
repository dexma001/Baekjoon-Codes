w=0

for _ in range(6):
    if str(input()) == 'W':
        w += 1

if 1<=w<=2:
    print(3)
elif 3<=w<=4:
    print(2)
elif 5<=w<=6:
    print(1)
else:
    print(-1)