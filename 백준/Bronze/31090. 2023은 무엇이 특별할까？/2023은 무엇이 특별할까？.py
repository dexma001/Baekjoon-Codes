for _ in range(int(input())):
    a = int(input())
    if (a+1) % (a % 100) == 0:
        print('Good')
    else:
        print('Bye')
