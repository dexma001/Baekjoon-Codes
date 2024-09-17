a, b, c = map(int, input().split())
m = 3*a+20*b+120*c
p, q, r = map(int, input().split())
me = 3*p+20*q+120*r

if m > me:
    print('Max')
elif m<me:
    print('Mel')
else:
    print('Draw')