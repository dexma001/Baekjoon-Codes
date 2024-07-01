n = int(input())

arr = list(map(int, input().split()))
arr_sum = sum(arr)
t, p = map(int, input().split())

answer1 = 0
for i in range(6):
    if arr[i] % t == 0:
        answer1 += arr[i]//t
    else:
        answer1 += arr[i]//t + 1

print(answer1)

print(arr_sum//p, arr_sum % p)
