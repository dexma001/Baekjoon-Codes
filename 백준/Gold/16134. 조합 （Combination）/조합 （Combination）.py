# 16134

n, r = map(int, input().split())
p = 1000000007

answer = 1
t1 = 1
t2 = 1

for i in range(1, n+1):
    t1 *= i
    t1 %= p

for j in range(1, r+1):
    t2 *= j
    t2 %= p

for k in range(1, n-r+1):
    t2 *= k
    t2 %= p


def mul(x, y, p):
    temp_ans = 1
    while y > 0:
        if y % 2 != 0:
            temp_ans *= x
            temp_ans %= p
        x *= x
        x %= p
        y //= 2
    return temp_ans


t3 = mul(t2, p-2, p)
t3 %= p
answer = t1*t3
answer %= p
print(answer)
