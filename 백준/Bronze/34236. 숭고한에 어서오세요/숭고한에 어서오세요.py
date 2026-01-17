n = int(input())
arr = list(map(int, input().split()))
temp = arr[1] - arr[0]
print(arr[-1] + temp)