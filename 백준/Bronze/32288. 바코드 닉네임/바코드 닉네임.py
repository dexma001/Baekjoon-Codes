n = int(input())
arr = list(map(str, input().strip()))

for i in range(n):
    if arr[i] == 'l':
        arr[i] = arr[i].upper()
    else:
        arr[i] = arr[i].lower()

print(''.join(arr))
