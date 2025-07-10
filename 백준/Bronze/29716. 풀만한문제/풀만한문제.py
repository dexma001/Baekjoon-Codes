j, n = map(int, input().split())
answer = 0

for _ in range(n):
    temp = list(map(str, input().strip()))
    temp_answer = 0

    for i in temp:
        if i == ' ':
            temp_answer += 1
        elif i.isdigit():
            temp_answer += 2
        else:
            if i.isupper():
                temp_answer += 4
            else:
                temp_answer += 2
    if temp_answer <= j:
        answer += 1
print(answer)
