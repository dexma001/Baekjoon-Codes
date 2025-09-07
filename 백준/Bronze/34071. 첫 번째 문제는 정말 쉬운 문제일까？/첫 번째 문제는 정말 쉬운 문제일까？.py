n = int(input())

temp = 0
answer = ''

for i in range(n):
    if i == 0:
        temp = int(input())
    elif i == 1:
        p = int(input())
        if p > temp:
            answer = 'ez'
        else:
            answer = 'hard'
    else:
        p = int(input())
        if p > temp:
            if answer == 'hard':
                answer = '?'
                print(answer)
                quit()
            else:
                continue
        else:
            if answer == 'ez':
                answer = '?'
                print(answer)
                quit()
            else:
                continue

print(answer)