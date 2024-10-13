breaker = ['E', 'N', 'D']
while True:
    temp = list(map(str, input().rstrip()))
    if not temp == breaker:
        print(''.join(temp[::-1]))
    else:
        break
