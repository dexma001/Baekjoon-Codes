arr = list()
for _ in range(5):
    arr.append(int(input()))
    
if arr[0] < 0:
    print(abs(arr[0])*arr[2] + arr[3] + arr[4]*arr[1])
elif arr[0] == 0:
    print(arr[3] + arr[4]*arr[1])
else:
    print((arr[1]-arr[0])*arr[4])