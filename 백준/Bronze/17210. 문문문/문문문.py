n = int(input())
k = int(input())

if n >= 6:
    print("Love is open door")
else:
    for i in range(n-1):
        if k == 0:
            print(1)
            k = 1
        else:
            print(0)
            k = 0