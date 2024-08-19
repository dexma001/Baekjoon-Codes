answer = list()

for _ in range(2):
    arr = list(map(int, input().split()))
    answer.append(arr[0]*6+arr[1]*3+arr[2]*2+arr[3]*1+arr[4]*2)

print(*answer)
