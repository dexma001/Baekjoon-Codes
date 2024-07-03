# 4673

import time

det_arr = list(0 for _ in range(10001))
for i in range(1, 10001):
    if det_arr[i] == 0:
        print(i)

        while True:
            temp = 0
            for j in str(i):
                temp += int(j)
            temp += i
            if temp < 10001:
                det_arr[temp] = 1
                i = temp
            else:
                break
    else:
        continue
