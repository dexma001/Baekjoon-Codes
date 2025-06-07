answer = list()

for i in range(5):
    temp = str(input())
    if 'FBI' in temp:
        answer.append(i+1)

print(*answer) if answer else print('HE GOT AWAY!')
