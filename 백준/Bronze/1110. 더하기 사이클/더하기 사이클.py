# 1110

import copy
import time
n = int(input())

answer = 0
temp = copy.deepcopy(n)
while True:
    if 0 <= temp <= 9:
        temp = 10*temp + temp
        answer += 1
    else:
        temp = 10*(temp % 10) + (((temp//10) + (temp % 10)) % 10)
        answer += 1

    if temp == n:
        print(answer)
        break
