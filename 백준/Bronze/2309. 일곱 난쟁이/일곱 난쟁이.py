arr = list()
for _ in range(9):
    arr.append(int(input()))
    
arr.sort()
arr_sum = sum(arr)

for i in range(8):
    for j in range(i+1, 9):
        if arr_sum-arr[i]-arr[j] == 100:
            arr.pop(i)
            arr.pop(j-1)

            for k in arr:
                print(k)
            quit()

