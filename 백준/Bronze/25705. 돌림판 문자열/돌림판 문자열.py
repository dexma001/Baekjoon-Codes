n = int(input())
arr = [0] + list(input())
m = int(input())
answer_arr = [0] + list(input())

temp_dict = dict()
for i in range(1, n+1):
    if arr[i] in temp_dict.keys():
        temp_dict[arr[i]].append(i)
    else:
        temp_dict[arr[i]] = [i]

answer = 0
wheel = n
for j in range(1, m+1):
    if answer_arr[j] not in temp_dict.keys():
        print(-1)
        quit()

    temp_answer = (10**10, 0)
    for i in temp_dict[answer_arr[j]]:
        if i == wheel:
            if n < temp_answer[0]:
                temp_answer = (n, i)
        elif i > wheel:
            if i-wheel < temp_answer[0]:
                temp_answer = (i-wheel, i)
        else:
            if i+n-wheel < temp_answer[0]:
                temp_answer = (i+n-wheel, i)

    answer += temp_answer[0]
    wheel = temp_answer[1]

print(answer)
