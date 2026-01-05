width, length = map(int, input().split())
t = int(input())
wid = list()
len = list()

temp = list()
for _ in range(t):
    temp.append(list(map(int, input().split())))

temp.append([0, length])
temp.append([1, width])
temp.sort(key=lambda x:[x[0], x[1]])

for i in range(t+2):
    a, b = temp[i]
    if a == 1:
        if not wid:
            wid.append(b)
        else:
            wid.append(b - temp[i-1][1])
    else:
        if not len:
            len.append(b)
        else:
            len.append(b - temp[i-1][1])

answer = 0

for i in wid:
    for j in len:
        answer = max(answer, i*j)

print(answer)