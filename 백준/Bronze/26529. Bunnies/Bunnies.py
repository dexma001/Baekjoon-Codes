arr = list()
arr.append(1)
arr.append(1)

for _ in range(44):
    arr.append(arr[-1] + arr[-2])
    
for _ in range(int(input())):
    print(arr[int(input())])