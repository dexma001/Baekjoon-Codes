n = int(input())
arr = list(map(int, input().split()))
arr.sort()

temp_sum = 0
answer = 0

for i in range(n):
    if arr[i] >= temp_sum:
        temp_sum += arr[i]
        answer += 1
        
print(answer)