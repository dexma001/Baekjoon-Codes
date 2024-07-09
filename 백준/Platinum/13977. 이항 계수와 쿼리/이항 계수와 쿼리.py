# 13977

import sys
input = sys.stdin.readline
p = 1000000007


def mul(x, y):
    ans = 1
    while y > 0:
        if y % 2 != 0:
            ans *= x
            ans %= p
        x *= x
        x %= p
        y = int(y / 2)
    return ans


dp = [0] * 4000001
dp[0] = 1
for i in range(1, 4000001):
    dp[i] = (dp[i-1] * i) % p

for _ in range(int(input())):
    n, r = map(int, input().split())

    ans = 1
    t1 = dp[n]
    t2 = (dp[r] * dp[n-r]) % p
    t3 = mul(t2, p-2) % p
    ans = (t1*t3) % p
    print(ans)
