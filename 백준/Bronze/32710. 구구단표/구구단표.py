arr = [2,3,4,5,6,7,8,9]
arr_1 = [1,2,3,4,5,6,7,8,9]

n = int(input())

for i in arr:
    for j in arr_1:
        if n == i*j:
            print(1)
            quit()
else:
    if n == 1:
        print(1)
    else:
        print(0)