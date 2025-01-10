a, b = map(int, input().split())

if a == 0 and b == 0:
    print('Not a moose')
    quit()

if a == b:
    print(f"Even {2*a}")

else:
    print(f"Odd {2*max(a, b)}")
