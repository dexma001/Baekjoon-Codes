import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a <= 2 or b <= 2:
        print('First')
    else:
        a1 = a % 2
        b1 = b % 2

        if a1 != 0:
            if b1 != 0:
                print('First')
            else:
                print('Second')
        else:
            print('Second')
