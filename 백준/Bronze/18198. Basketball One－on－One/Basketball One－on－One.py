arr = list(map(str, input().strip()))
A = 0
B = 0

for k in range(len(arr)//2):
    i, j = arr[2*k:2*k+2][0], arr[2*k:2*k+2][1]

    if i == 'A':
        A += int(j)
    else:
        B += int(j)

print("A") if A > B else print("B")
