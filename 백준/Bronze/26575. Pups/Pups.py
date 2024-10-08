for _ in range(int(input())):
    a, b, c = map(float, input().split())
    answer = a*b*c
    print('$%.2f' % answer)
