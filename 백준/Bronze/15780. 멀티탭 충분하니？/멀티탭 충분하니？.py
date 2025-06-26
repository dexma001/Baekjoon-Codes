import math

n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer =0
for i in arr:
    answer += math.ceil(i/2)

print("YES") if answer >= n else print("NO")