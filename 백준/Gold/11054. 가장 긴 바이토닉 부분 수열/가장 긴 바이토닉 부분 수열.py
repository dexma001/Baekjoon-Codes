import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li_rev = li[::-1]

inc = [1 for i in range(n)]
dec = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if li_rev[i] > li_rev[j]:
            dec[i] = max(dec[i], dec[j]+1)
ans = 0
for l in range(n):
    ans = max(ans, (inc[l] + dec[n-l-1] - 1))

print(ans)
