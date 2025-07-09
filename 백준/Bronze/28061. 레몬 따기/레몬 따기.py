n = int(input())
arr = list(map(int, input().split()))

answer = 0

for i in range(n):
    answer = max(answer, max(arr[i] - (n-i), 0))
print(answer)