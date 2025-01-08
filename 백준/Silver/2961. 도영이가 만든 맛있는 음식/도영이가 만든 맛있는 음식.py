import sys
input = sys.stdin.readline

arr = list()

n = int(input())
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: [x[0], x[1]])

answer = sys.maxsize

for i in range(1, 1 << n):
    s = 1
    b = 0
    for j in range(n):
        if i & (1 << j) != 0:
            s *= arr[j][0]
            b += arr[j][1]
    answer = min(answer, abs(s-b))

print(answer)
