one = 0
zero = 0

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        one += 1
    else:
        zero += 1
        
if one > zero:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')