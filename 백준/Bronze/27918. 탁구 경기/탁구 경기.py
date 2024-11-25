import sys
input = sys.stdin.readline

n = int(input())
a1 = 0
a2 = 0

for _ in range(n):
    temp = str(input().strip())
    if temp == 'D':
        a1 += 1
    else:
        a2 += 1

    if abs(a1-a2) == 2:
        break

print(f"{a1}:{a2}")
