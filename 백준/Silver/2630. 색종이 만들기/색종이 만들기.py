# 2630

import sys
input = sys.stdin.readline

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))

white = 0
blue = 0


def cut(x, y, n):
    global white, blue
    color = arr[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != color:
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return

    if color == 1:
        blue += 1
    else:
        white += 1


cut(0, 0, n)
print(white)
print(blue)
