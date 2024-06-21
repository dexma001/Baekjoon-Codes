stroke = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1,
          2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

a = list(input().rstrip())
b = list(input().rstrip())

dp = list()

for i in range(len(a)):
    dp.append(stroke[ord(a[i]) - 65])
    dp.append(stroke[ord(b[i]) - 65])

while len(dp) != 2:
    temp_dp = list()
    for i in range(0, len(dp)-1):
        temp_dp.append((dp[i] + dp[i+1]) % 10)
    dp = temp_dp

print('{}{}'.format(dp[0], dp[1]))
