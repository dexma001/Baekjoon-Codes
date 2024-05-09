# 2342

import sys
input = sys.stdin.readline


move_fee = [[0, 2, 2, 2, 2], [0, 1, 3, 4, 3], [
    0, 3, 1, 3, 4], [0, 4, 3, 1, 3], [0, 3, 4, 3, 1]]

question_arr = list(map(int, input().split()))
question_arr.pop()
len_question = len(question_arr)

dp = list([[10**8] * 5 for _ in range(5)] for _ in range(len_question))

dp[0][question_arr[0]][0] = 2
dp[0][0][question_arr[0]] = 2


def dynamic(i):
    for x in range(5):
        for y in range(5):
            move_left_power = move_fee[x][question_arr[i]]
            dp[i][question_arr[i]][y] = min(
                dp[i][question_arr[i]][y], dp[i-1][x][y] + move_left_power)
            move_right_power = move_fee[y][question_arr[i]]
            dp[i][x][question_arr[i]] = min(
                dp[i][x][question_arr[i]], dp[i-1][x][y] + move_right_power)


for i in range(1, len_question):
    dynamic(i)

min_value = min(map(min, dp[-1]))
print(min_value)
