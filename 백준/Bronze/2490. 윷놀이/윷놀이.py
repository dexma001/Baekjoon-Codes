# 2490

for _ in range(3):
    arr = list(map(int, input().split()))
    temp = arr.count(0)

    if temp == 0:
        print('E')
    elif temp == 1:
        print('A')
    elif temp == 2:
        print('B')
    elif temp == 3:
        print('C')
    else:
        print('D')
