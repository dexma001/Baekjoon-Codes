# 11866

import sys

n, m = map(int, input().split())
arr = list(i for i in range(1, n+1))
temp = n

answer_arr = list()

k = 0
while temp > 0:
    k = (k+m) % (temp) if (k+m) % temp != 0 else temp
    answer_arr.append(arr.pop(k-1))
    temp -= 1
    k -= 1

answer = "{}".format(answer_arr[0])

for i in range(1, n):
    answer += ", {}".format(answer_arr[i])

print("<" + answer + ">")
