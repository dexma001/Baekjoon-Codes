#13976

import sys
input = sys.stdin.readline

t = int(input())
if t%2 != 0:
    print(0)
elif t == 2:
    print(3)
elif t == 4:
    print(11)
else:
    def matrix_mult(a, b):
        temp = [(a[0]*b[0]+a[1]*b[2]) % 1000000007, (a[0]*b[1]+a[1]*b[3]) % 1000000007,
                (a[2]*b[0]+a[3]*b[2]) % 1000000007, (a[2]*b[1]+a[3]*b[3]) % 1000000007]
        return temp

    def matrix_pow(n, m):
        if n == 1:
            return m
        else:
            k = matrix_pow(n//2, m)
            if n%2 == 0:
                return matrix_mult(k, k)
            else:
                return matrix_mult(matrix_mult(k, k), m)
            
    a = [4, -1, 1, 0]
    u = matrix_pow((t//2)-2, a)

    print((u[0]*11 + u[1]*3)%1000000007)