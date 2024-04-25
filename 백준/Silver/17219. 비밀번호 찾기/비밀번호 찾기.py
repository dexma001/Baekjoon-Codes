# 17219

import sys
input = sys.stdin.readline

password_list = dict()

n, m = map(int, input().split())

for _ in range(n):
    a, b = input().split()
    password_list[a] = b

for _ in range(m):
    print(password_list[input().rstrip()])
