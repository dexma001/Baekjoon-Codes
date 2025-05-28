n = int(input())
arr = list(map(int, input().split()))
while len(arr) != 5:
    arr.append(0)

answer = 0

if arr[0] > arr[2]:
    answer += (arr[0] - arr[2])*508
else:
    answer += (arr[2] - arr[0]) * 108
if arr[1] > arr[3]:
    answer += (arr[1] - arr[3]) * 212
else:
    answer += (arr[3] - arr[1]) * 305
if arr[-1]:
    answer += arr[-1] * 707

print(answer * 4763)
