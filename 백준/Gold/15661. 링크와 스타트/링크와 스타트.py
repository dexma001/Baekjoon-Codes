# 15661

import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = int(sys.maxsize)
temp = 1

while temp < ((1 << n)-1):
    sum_ = 0
    for i in range(n):
        for j in range(i+1, n):
            is_i = 1 if temp & (1 << i) else 0
            is_j = 1 if temp & (1 << j) else 0

            if is_i == is_j:
                if is_i:
                    sum_ += (arr[i][j] + arr[j][i]) * (1)
                else:
                    sum_ += (arr[i][j] + arr[j][i]) * (-1)

    answer = min(answer, abs(sum_))
    temp += 1

print(answer)
