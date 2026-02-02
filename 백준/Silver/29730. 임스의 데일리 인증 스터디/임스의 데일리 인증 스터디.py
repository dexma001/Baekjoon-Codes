n = int(input())

baek = list()
another = list()

for _ in range(n):
    temp = str(input())
    if ("boj.kr/") in temp:
        baek.append(int(temp[7:]))
    else:
        another.append([temp, len(temp)])
        
another.sort(key = lambda x:[x[1], x[0]])
baek.sort()

for i in another:
    print(i[0])
for i in baek:
    print("boj.kr/" + str(i))