# 1644

from collections import deque

n = int(input())
li = list(x for x in range(n+1))
cnt = 0

for i in range(2, int(n**(1/2))+1):
    if li[i] == 0:
        continue
    for j in range(i*i, n+1, i):
        li[j] = 0

li_prime = list()

for k in range(2, len(li)):
    if li[k] == 0:
        continue
    else:
        li_prime.append(li[k])
li_prime.sort()


sigma = deque([])

for i in range(len(li_prime)):
    sigma.append(li_prime[i])
    while True:
        if sum(sigma) > n:
            sigma.popleft()
        elif sum(sigma) == n:
            cnt += 1
            break
        else:
            break

print(cnt)
