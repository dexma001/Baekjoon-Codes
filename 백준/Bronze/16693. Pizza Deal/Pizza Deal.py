import math

a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())

t1 = a1/p1
t2 = r1*r1*math.pi/p2

print('Whole pizza') if t2 > t1 else print('Slice of pizza')