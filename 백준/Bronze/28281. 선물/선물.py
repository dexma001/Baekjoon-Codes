n,m = map(int, input().split())
arr = list(map(int, input().split()))
temp = 100000000

for i in range(n-1):
    temp = min(temp, arr[i] + arr[i+1])

print(temp*m)