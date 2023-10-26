import sys
from itertools import combinations
n, m = map(int, input().split())
li = list(sys.stdin.readline().strip().split())
li_m = list()
li_s = list()
li_m1 = ['a', 'e', 'i', 'o', 'u']

for i in range(len(li)):
    if li[i] in li_m1:
        li_m.append(li[i])
    else:
        li_s.append(li[i])

li_m_p = []
li_s_p = []
li_p = []


def com(x):

    if len(li_m) > x-2:
        for i in range(1, n-1):
            j = n-i
            a = list(combinations(li_m, i))
            b = list(combinations(li_s, j))
            for p in range(len(a)):
                for q in range(len(b)):
                    li_p.append(a[p]+b[q])

    else:
        for i in range(1, len(li_m)+1):
            j = n-i
            a = list(combinations(li_m, i))
            b = list(combinations(li_s, j))
            for p in range(len(a)):
                for q in range(len(b)):
                    li_p.append(a[p]+b[q])

    for i in range(len(li_p)):
        li_p[i] = list(li_p[i])
        li_p[i] = sorted(li_p[i])
        li_p[i] = ''.join(li_p[i])

    li_p.sort()
    return li_p


com(n)
for i in range(len(li_p)):
    print(li_p[i])
