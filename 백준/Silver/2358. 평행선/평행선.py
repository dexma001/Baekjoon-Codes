from collections import defaultdict

x = defaultdict(int)
y = defaultdict(int)

for _ in range(int(input())):
    a, b = map(int, input().split())
    x[a] += 1
    y[b] += 1
    
answer = 0
for i, j in enumerate(x):
    if x[j] >= 2:
        answer += 1

for i, j in enumerate(y):
    if y[j] >= 2:
        answer += 1

print(answer)