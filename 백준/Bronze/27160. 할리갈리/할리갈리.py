from collections import defaultdict

n = int(input())
arr = defaultdict(int)

for _ in range(n):
    a, b = map(str, input().split())
    arr[a] += int(b)

trig = 0
for i in list(arr.keys()):
    if arr[i] == 5:
        trig = 1

print('YES') if trig else print('NO')
