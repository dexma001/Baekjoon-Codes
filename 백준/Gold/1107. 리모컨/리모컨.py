# 1107

target = int(input())
ans = abs(target - 100)
m = int(input())
li = set()

if m != 0:
    li = set(input().split())

for i in range(1000001):
    for n in str(i):
        if n in li:
            break
    else:
        ans = min(ans, len(str(i)) + abs(i - target))

print(ans)
