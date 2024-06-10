# 8989

n = int(input())
for _ in range(n):
    arr = list(map(str, input().split()))
    answer_arr = list()
    for i in range(5):
        n, m = map(int, arr[i].split(':'))
        if n >= 12:
            time_angle = 30 * (n-12)
        else:
            time_angle = 30 * n
        time_angle += 0.5*m

        minute_angle = 6*m

        answer = abs(time_angle - minute_angle)
        answer = min(answer, abs(360-answer))

        answer_arr.append((answer, n, m, arr[i]))

    answer_arr.sort(key=lambda x: (x[0], x[1], x[2]))
    print(answer_arr[2][3])
