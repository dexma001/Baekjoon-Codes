arr = list(map(int, input().split()))
answer =0
for i in arr:
    answer += (max(arr) - i)
print(answer)