import math

n = int(input())
arr = list(map(int, input().split()))

M = 0
Y = 0

for i in range(n):
    y = arr[i]
    m = arr[i]
    y_cnt = 0
    m_cnt = 0
    while y > 29:
        y -= 30
        y_cnt += 1
    while m > 59:
        m -= 60
        m_cnt += 1
    Y += (y_cnt+1)*10
    M += (m_cnt+1)*15

if M == Y:
    print(f"Y M {M}")
elif M < Y:
    print(f"M {M}")
else:
    print(f"Y {Y}")
