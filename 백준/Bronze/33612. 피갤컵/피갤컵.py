import sys
input = sys.stdin.readline

n = int(input())
arr = [2024, 8]

for _ in range(n-1):
    arr = [arr[0] + ((arr[1]+7)//12), (arr[1]+7) % 12]
    if arr[1] == 0:
        arr[0] -= 1
        arr[1] = 12

print(*arr)
