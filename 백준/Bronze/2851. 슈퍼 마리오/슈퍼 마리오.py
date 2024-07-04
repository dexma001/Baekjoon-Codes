answer = 0

temp_answer = 0
for _ in range(10):
    temp = int(input())
    if answer != 0:
        continue
    if temp_answer + temp > 100:
        if abs(temp_answer+temp-100) <= abs(temp_answer-100):
            answer = temp_answer+temp
        else:
            answer = temp_answer
    else:
        temp_answer += temp

if answer == 0 and temp+answer < 100:
    answer = temp_answer

print(answer)
