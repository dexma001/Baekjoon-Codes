arr = list(map(str, input().strip()))
count = 0
answer = ''


for i in arr:
    if i == 'X':
        count += 1
    else:
        if count % 2 != 0:
            print('-1')
            quit()

        answer += 'AAAA'*(count//4)
        answer += 'BB'*((count % 4)//2)
        count = 0
        answer += i

if count:
    if count % 2 != 0:
        print('-1')
        quit()
    answer += 'AAAA'*(count//4)
    answer += 'BB'*((count % 4)//2)

print(answer)
