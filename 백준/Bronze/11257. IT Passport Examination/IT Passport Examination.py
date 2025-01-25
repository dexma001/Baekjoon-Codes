for _ in range(int(input())):
    a,b,c,d=map(int, input().split())
    if b+c+d >= 55 and b>= 11 and c>= 8 and d>=12:
        print(a, b+c+d, 'PASS')
    else:
        print(a, b+c+d, 'FAIL')