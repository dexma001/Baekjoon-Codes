n = int(input())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
answer = 0

for i in range(n):
    if arr_2[i] >= arr_1[i]:
        answer += 1

print(answer)