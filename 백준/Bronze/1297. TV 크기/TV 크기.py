import math

d, h, w = map(int, input().split())

t = (d**2 / (h**2 + w**2))**(0.5)

x = t*h
y = t*w

print(math.floor(x), math.floor(y))