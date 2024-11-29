a, b = map(int, input().split())

k, x = map(int, input().split())

if k + x < a:
    print('IMPOSSIBLE')
    quit()

if k-x > b:
    print('IMPOSSIBLE')
    quit()

else:
    print(min(b, k+x) - max(k-x, a) + 1)
