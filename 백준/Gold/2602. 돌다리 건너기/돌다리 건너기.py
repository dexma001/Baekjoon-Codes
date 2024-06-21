# 2602

import sys
input = sys.stdin.readline

scroll = ['\0'] + list(input().rstrip())
ang = ['\0'] + list(input().rstrip())
dev = ['\0'] + list(input().rstrip())

ang_dp = list([0] * (len(ang)) for _ in range(len(scroll)))
dev_dp = list([0] * (len(dev)) for _ in range(len(scroll)))

for i in range(1, len(scroll)):
    if i == 1:
        for j in range(1, len(ang)):
            if scroll[i] == ang[j]:
                ang_dp[i][j] = ang_dp[i][j-1] + 1
            else:
                ang_dp[i][j] = ang_dp[i][j-1]

            if scroll[i] == dev[j]:
                dev_dp[i][j] = dev_dp[i][j-1] + 1
            else:
                dev_dp[i][j] = dev_dp[i][j-1]
    else:
        for j in range(1, len(ang)):
            if i % 2 != 0:
                if scroll[i] == ang[j]:
                    ang_dp[i][j] = ang_dp[i][j-1] + ang_dp[i-1][j-1]
                else:
                    ang_dp[i][j] = ang_dp[i][j-1]

                if scroll[i] == dev[j]:
                    dev_dp[i][j] = dev_dp[i][j-1] + dev_dp[i-1][j-1]
                else:
                    dev_dp[i][j] = dev_dp[i][j-1]
            else:
                if scroll[i] == dev[j]:
                    ang_dp[i][j] = ang_dp[i][j-1] + ang_dp[i-1][j-1]
                else:
                    ang_dp[i][j] = ang_dp[i][j-1]

                if scroll[i] == ang[j]:
                    dev_dp[i][j] = dev_dp[i][j-1] + dev_dp[i-1][j-1]
                else:
                    dev_dp[i][j] = dev_dp[i][j-1]

print(ang_dp[-1][-1] + dev_dp[-1][-1])
