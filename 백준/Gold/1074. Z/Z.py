# 1074

import sys
input = sys.stdin.readline

n, r, c = list(map(int, input().split()))
length = 2**n

answer = 0

while True:
    if 0 <= r <= 1 and 0 <= c <= 1:
        answer += ((2*r)+(c*1))
        break

    if r < length//2:
        if c < length//2:
            pass
        else:
            answer += ((length**2)//4)
            c -= length//2
    else:
        answer += ((length**2) // 2)
        r -= length//2
        if c < length//2:
            pass
        else:
            answer += ((length**2)//4)
            c -= length//2

    length //= 2

print(answer)
