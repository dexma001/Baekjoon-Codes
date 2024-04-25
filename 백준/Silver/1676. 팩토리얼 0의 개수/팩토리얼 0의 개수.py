# 1676

arr = int(input())
cnt_5 = 0
cnt_2 = 0

for i in range(1, arr+1):
    if i % 5 == 0:
        while i % 5 == 0:
            cnt_5 += 1
            i = i // 5
    if i % 2 == 0:
        while i % 2 == 0:
            cnt_2 += 1
            i = i // 2
    else:
        continue

print(min(cnt_5, cnt_2))
