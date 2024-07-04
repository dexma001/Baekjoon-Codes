temp = input().rstrip()
k = len(temp)

if k > 10:
    for i in range(k//10):
        print(temp[10*i:10*i+10])

    print(temp[10*(i+1):])
else:
    print(temp)
