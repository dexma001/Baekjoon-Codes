import math

n = int(input())
if n == 1:
    print(0)
else:
    temp = n*n
    print(math.ceil(temp/2))
