import sys
input = sys.stdin.readline

n = str(input().strip())
m = str(input().strip())

nl = len(n)
ml = len(m)

answer = 0
t = 0

if ml > nl:
    print(answer)
else:
    temp = 0
    while temp+ml <= nl:
        if n[temp:temp+ml] == m:
            answer += 1
            temp += ml
        else:
            temp += 1

    print(answer)