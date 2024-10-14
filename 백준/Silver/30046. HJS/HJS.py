# 30046

import sys
input = sys.stdin.readline

n = int(input())
p = list(map(str, input().rstrip()))
q = list(map(str, input().rstrip()))
r = list(map(str, input().rstrip()))

for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            for k in range(1, 4):
                if i != k and j != k:
                    alpha = dict()
                    alpha['H'] = str(i)
                    alpha['J'] = str(j)
                    alpha['S'] = str(k)
                    p1 = list()
                    q1 = list()
                    r1 = list()
                    for l in range(n):
                        p1.append(alpha[p[l]])
                        q1.append(alpha[q[l]])
                        r1.append(alpha[r[l]])

                    p1 = ''.join(p1)
                    q1 = ''.join(q1)
                    r1 = ''.join(r1)

                    if p1 < q1 and q1 < r1:
                        print("HJS! HJS! HJS!")
                        quit()

else:
    print("Hmm...")
