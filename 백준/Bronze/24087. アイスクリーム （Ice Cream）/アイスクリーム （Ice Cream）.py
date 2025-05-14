import math

s = int(input())
a = int(input())
b = int(input())

if a >= s:
    print(250)
else:
    print(math.ceil((s-a)/b) * 100 + 250)
