dp = list(0 for _ in range(491))
dp[1] = 1
dp[2] = 1
for i in range(3, 491):
    dp[i] = dp[i-1] + dp[i-2]

while True:
    n = int(input())
    if n <= 0:
        break
    print(f"Hour {n}: {dp[n]} cow(s) affected")