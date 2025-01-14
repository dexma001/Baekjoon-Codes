n, k, i = map(int, input().split())
if k > i:
    k, i = i, k
answer = 1

while True:
    if k % 2 != 0 and k == i-1:
        break

    if k % 2 == 0:
        k = k//2
    else:
        k = (k+1)//2

    if i % 2 == 0:
        i = i//2
    else:
        i = (i+1)//2
    answer += 1

print(answer)
