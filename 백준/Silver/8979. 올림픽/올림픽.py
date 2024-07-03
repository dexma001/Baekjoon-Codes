# 8979

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list()

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: [x[1], x[2], x[3]], reverse=True)


answer = 1
if arr[0][0] == k:
    1
else:
    temp = 1
    for i in range(1, n):
        if arr[i][0] == k:
            if arr[i-1][1:] == arr[i][1:]:
                break
            else:
                answer += temp
                break

        if arr[i-1][1:] == arr[i][1:]:
            temp += 1
        else:
            answer += temp
            temp = 1


print(answer)
