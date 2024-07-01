# 28702

import sys
input = sys.stdin.readline

temp = 0
for i in range(3):
    n = input().rstrip()
    if n.isdigit() == True:
        temp = int(n) + (3-i)


if temp % 5 == 0:
    if temp % 3 == 0:
        print('FizzBuzz')
    else:
        print('Buzz')
else:
    if temp % 3 == 0:
        print('Fizz')
    else:
        print(temp)
