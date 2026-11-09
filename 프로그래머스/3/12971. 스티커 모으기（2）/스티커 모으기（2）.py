def solution(sticker):
    answer = 0
    
    dp = [[0 for _ in range(len(sticker))] for _ in range(2)]
    
    if len(sticker) <= 2:
        answer = max(sticker)
    
    else:   
        for i in range(len(sticker)):
            if i == 0:
                dp[0][i] = sticker[i]
            elif i == 1:
                dp[0][i] = dp[0][i-1]
                dp[1][i] = sticker[i]
            elif i == len(sticker) - 1:
                dp[1][i] = max(dp[1][i-1], dp[1][i-2] + sticker[i])
            else:
                dp[0][i] = max(dp[0][i-1], dp[0][i-2] + sticker[i])
                dp[1][i] = max(dp[1][i-1], dp[1][i-2] + sticker[i])
        answer = max(dp[0][-1], dp[0][-2], dp[1][-1], dp[1][-2])
    return answer