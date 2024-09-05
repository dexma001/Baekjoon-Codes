# 10994

n = int(input())
l = 1+4*(n-1)

arr = list(list(' ' for _ in range(l)) for _ in range(l))

for i in range(0, l//2+1, 2):
    for j in range(i, l-i):
        arr[i][j] = '*'
        arr[l-i-1][j] = '*'
        arr[j][l-i-1] = '*'
        arr[j][i] = '*'

for i in arr:
    print(''.join(i))
