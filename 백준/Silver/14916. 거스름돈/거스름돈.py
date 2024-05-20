# 14916

n = int(input())
m = n // 5

arr = [0] * (m+1)
for i in range(m+1):
    temp = n - 5*i
    if temp % 2 != 0:
        arr[i] = 50000
    else:
        arr[i] = i + temp//2

k = min(arr)
if k == 50000:
    print(-1)
else:
    print(min(arr))
