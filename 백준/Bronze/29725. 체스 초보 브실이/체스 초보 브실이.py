point = {'K': 0, 'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9}
temp = list(point.keys())

white = 0
black = 0


for _ in range(8):
    arr = list(map(str, input().strip()))
    for i in arr:
        if i.upper() in temp:
            if i.upper() == i:
                white += point[i]
            else:
                black += point[(i.upper())]

print(white-black)
