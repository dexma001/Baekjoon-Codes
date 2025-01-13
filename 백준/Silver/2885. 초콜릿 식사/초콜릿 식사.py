k = int(input())
n = 1
answer = list()

while 1 << n < k:
    n += 1

temp = 1 << n
answer.append(temp)

cnt = 0
while True:
    if temp <= k:
        k -= temp

    if k == 0:
        answer.append(cnt)
        break
    cnt += 1
    temp >>= 1

print(*answer)
