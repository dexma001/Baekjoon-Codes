#17357

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

acu =[0] + list(0 for _ in range(n))
acu_sq = [0] +list(0 for _ in range(n))


for i in range(1, n+1):
    acu[i] = acu[i-1] + arr[i]
    acu_sq[i] = acu_sq[i-1] + arr[i] * arr[i]

for i in range(1, n+1):
    answer = 1
    mm = 0
    for j in range(1, n-i+2):
        av1 = acu[j+i-1] - acu[j-1]
        av2 = acu_sq[j+i-1] - acu_sq[j-1]
        tmp = av2*i - av1*av1
        if tmp > mm:
            answer = j
            mm = tmp
    print(answer)