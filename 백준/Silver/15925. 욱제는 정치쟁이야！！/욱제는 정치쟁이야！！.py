#15925

import sys
input = sys.stdin.readline

n, ox = map(int, input().split())
arr = list()
height = list(0 for _ in range(n))
width = list(0 for _ in range(n))

for j in range(n):
    temp = list(map(int, input().split()))
    for i in range(n):
        if ox == temp[i]:
            width[i] += 1
            height[j] += 1

    arr.append(temp)

while True:
    cng = 0
    for i in range(n):
        if width[i] > n//2:
            for j in range(n):
                if arr[j][i] != ox:
                    arr[j][i] = ox
                    height[j] += 1
                    cng += 1

    for i in range(n):
        if height[i] > n//2:
            for j in range(n):
                if arr[i][j] != ox:
                    arr[i][j] = ox
                    width[j] += 1
                    cng += 1
    
    if cng == 0:
        break

for i in range(n):
    for j in range(n):
        if arr[i][j] != ox:
            print(0)
            quit()

else:
    print(1)
