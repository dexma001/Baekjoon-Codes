n = int(input())
if n == 1:
    print('*')
else:
    for i in range(n):
        if i == 0:
            print(' '*(n-1) + '*')
        elif i == n-1:
            print('*'*(1+2*(n-1)))
        else:
            print(' '*(n-i-1) + '*' + ' '*(1+2*(i-1)) + '*')