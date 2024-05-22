# 2133

n = int(input())

if n % 2 != 0:
    print(0)

else:
    temp = n//2
    dp = [0] * (temp+1)
    for i in range(1, temp+1):
        if i == 1:
            dp[i] = 3
        elif i == 2:
            dp[i] = 11
        else:
            dp[i] = dp[i-1] * 4 - dp[i-2]

    print(dp[-1])
