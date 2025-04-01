for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    temp = sum(arr)

    if temp == 0:
        print('Equilibrium')
    elif temp > 0:
        print('Right')
    else:
        print('Left')
