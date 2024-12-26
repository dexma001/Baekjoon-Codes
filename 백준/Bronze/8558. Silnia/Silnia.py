import math

n = int(input())
if n <= 4:
    print(str(math.factorial(n))[-1])
else:
    print('0')
