# 2921

arr = list(0 for _ in range(1001))
dp = list(0 for _ in range(1001))

arr[1] = 3
dp[1] = 3

temp = 6

for i in range(2, 1001):
    arr[i] = arr[i-1] + temp
    dp[i] = dp[i-1] + arr[i]
    temp += 3

print(dp[int(input())])
