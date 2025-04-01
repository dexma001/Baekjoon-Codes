# 1111

n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print('A')
elif n == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print('A')
else:
    if arr[0] == arr[1]:
        if arr.count(arr[0]) != n:
            print('B')
        else:
            print(arr[0])
    else:
        if arr[1] == arr[2]:
            if arr.count(arr[1]) != n-1:
                print('B')
            else:
                print(arr[1])
        else:
            alpha = arr[0]
            beta = arr[1]
            gamma = arr[2]

            a = (beta-gamma) / (alpha-beta)
            breaker = 0
            if not int(a) == a:
                breaker = 1
            a = int(a)
            b = beta - a*alpha

            for i in range(n-1):
                if not breaker and arr[i]*a+b != arr[i+1]:
                    breaker = 1

            if breaker:
                print('B')
            else:
                print(arr[-1]*a+b)
