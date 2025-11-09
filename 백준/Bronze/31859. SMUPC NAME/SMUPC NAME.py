from collections import defaultdict
import sys
input = sys.stdin.readline

n, name = input().split()
result = ""

aban = 0
for i in name:
    if i not in result:
        result += i
    else:
        aban += 1

result = str(int(n) + 1906) + result + str(aban+4)
result = "smupc_" + result[::-1]

print(result)
