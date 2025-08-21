import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = 0

for i in range(n-1, 0, -1):
    if arr[i] < arr[i-1]:
        arr[i-1] = arr[i]

print(sum(arr))
