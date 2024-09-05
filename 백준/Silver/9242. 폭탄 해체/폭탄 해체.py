# 9242

import sys
input = sys.stdin.readline

arr = list(input() for _ in range(5))
n = ((len(arr[0])-1)//4) + 1

answer = list()

zero = ['***', '* *', '* *', '* *', '***']
one = ['  *', '  *', '  *', '  *', '  *']
two = ['***', '  *', '***', '*  ', '***']
three = ['***', '  *', '***', '  *', '***']
four = ['* *', '* *', '***', '  *', '  *']
five = ['***', '*  ', '***', '  *', '***']
six = ['***', '*  ', '***', '* *', '***']
seven = ['***', '  *', '  *', '  *', '  *']
eight = ['***', '* *', '***', '* *', '***']
nine = ['***', '* *', '***', '  *', '***']
nums = [zero, one, two, three, four, five, six, seven, eight, nine]

check = list(False for _ in range(5))
ch_num = list(False for _ in range(10))
for i in range(n):
    for k in range(10):
        for j in range(5):
            if arr[j][i*4:i*4+3] == nums[k][j]:
                check[j] = True
        if all(check):
            ch_num[k] = True
            answer.append(str(k))
        check = list(False for _ in range(5))
    if any(ch_num):
        ch_num = list(False for _ in range(10))
        continue
    else:
        print('BOOM!!')
        quit()

ans = int(''.join(answer))

if ans % 6 == 0:
    print('BEER!!')
else:
    print('BOOM!!')
