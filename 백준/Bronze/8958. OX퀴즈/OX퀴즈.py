n = int(input())

for i in range(n):
    li = list(map(str, input().strip()))
    ans = 0
    k = 1
    for i in range(len(li)):
        if li[i] == 'O':
            ans += k
            k += 1
        else:
            k = 1
    print(ans)
