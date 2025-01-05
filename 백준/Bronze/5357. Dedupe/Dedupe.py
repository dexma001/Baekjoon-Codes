for _ in range(int(input())):
    temp = str(input())
    answer = ''

    for i in range(len(temp)):
        if not answer:
            answer += temp[i]
        else:
            if answer[-1] != temp[i]:
                answer += temp[i]

    print(answer)
