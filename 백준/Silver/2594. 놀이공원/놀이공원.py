# 2594

import sys
input = sys.stdin.readline

arr = [[600, 600], [1320, 1320]]
for _ in range(int(input())):
    a, b = map(str, input().split())
    a1 = int(a[:2])*60+int(a[2:])-10
    b1 = int(b[:2])*60+int(b[2:])+10
    arr.append([a1, b1])
arr.sort(key=lambda x: [x[0], x[1]])

answer = 0
end = 600

for i, j in arr:
    answer = max(answer, i-end)
    end = max(end, j)

print(answer)
