# 1622

import sys

while True:
    try:
        a = list(map(str, input().strip()))
        b = list(map(str, input().strip()))
        a.sort()
        b.sort()
        answer = ''

        while a and b:
            if a[0] == b[0]:
                answer += a[0]
                a.pop(0)
                b.pop(0)
            elif ord(a[0]) > ord(b[0]):
                b.pop(0)
            elif ord(a[0]) < ord(b[0]):
                a.pop(0)
        print(answer)

    except:
        break
