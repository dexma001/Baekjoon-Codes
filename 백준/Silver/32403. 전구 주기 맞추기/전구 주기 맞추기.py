n, t = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

for i in arr:
    temp_answer = 0
    if i == 1:
        continue
    while temp_answer != i:
        if t % (i-temp_answer) == 0 or t % (i + temp_answer) == 0:
            answer += temp_answer
            temp_answer = i
        else:
            temp_answer += 1

print(answer)
