temp = list(map(str, input().strip()))
temp.sort(reverse=True)
if temp[-1] == '0' and int(''.join(temp)) % 3 == 0:
    print(''.join(temp))
else:
    print(-1)
