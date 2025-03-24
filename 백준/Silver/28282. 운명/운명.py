from collections import defaultdict

x, k = map(int, input().split())
arr = list(map(int, input().split()))

left_arr = defaultdict(int)
right_arr = defaultdict(int)

for i in range(x):
    left_arr[arr[i]] += 1

for j in range(x, 2*x):
    right_arr[arr[j]] += 1

left_arr_1 = list(left_arr.keys())

answer = 0

for i in left_arr_1:
    answer += left_arr[i] * (x - right_arr[i])

print(answer)
