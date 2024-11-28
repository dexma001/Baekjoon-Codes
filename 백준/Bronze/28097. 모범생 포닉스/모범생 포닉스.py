n = int(input())
arr = list(map(int, input().split()))

answer = sum(arr) + 8*(n-1)

print(answer//24, answer % 24)
