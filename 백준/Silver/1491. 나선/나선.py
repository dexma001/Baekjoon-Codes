# 1491

import sys

n, m = map(int, input().split())

if n == 1 and m == 1:
    print(0, 0)
elif n == 1:
    print(0, m-1)
elif m == 1:
    print(n-1, 0)
else:
    if n == m:
        if n % 2 == 0:
            print(n//2-1, n//2)
        else:
            print((n-1)//2, (n-1)//2)

    else:
        p, q = 0, 0

        while (n+m)*2-4 < n*m:
            n -= 2
            m -= 2
            p += 1
            q += 1

        if n > m:
            if m % 2 == 0:
                q += 1
            else:
                p += n-1
        else:
            if n % 2 == 0:
                q += 1
            else:
                q += m-1

        print(p, q)
