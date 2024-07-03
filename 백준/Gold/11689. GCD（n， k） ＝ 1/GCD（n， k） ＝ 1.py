# 11689

from collections import defaultdict
import math
import sys
input = sys.stdin.readline

n = int(input())
temp = defaultdict(int)

x = math.ceil(math.sqrt(n)) + 1

for i in range(2, x):
    while n % i == 0:
        temp[i] += 1
        n //= i

if n != 1:
    temp[n] = 1

answer = 1

for i in temp.keys():
    answer *= i**temp[i] - (i**(temp[i]-1))

print(answer)
