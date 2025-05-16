answer, answer_cnt = '', 0

for _ in range(7):
    a, b = map(str, input().split())
    if int(b) > answer_cnt:
        answer = a
        answer_cnt  = int(b)


print(answer)