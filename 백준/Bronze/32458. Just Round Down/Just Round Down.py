temp = list(map(str, input().rstrip()))

answer = ''
for i in temp:
    if i == '.':
        break
    else:
        answer += i

print(answer)
