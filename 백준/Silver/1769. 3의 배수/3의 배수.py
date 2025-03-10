import time

n = int(input())

cnt = 0

while len(str(n)) != 1:
    temp = 0
    for i in str(n):
        temp += int(i)
    n = temp
    cnt += 1


print(cnt)
print('NO') if n % 3 != 0 else print('YES')
