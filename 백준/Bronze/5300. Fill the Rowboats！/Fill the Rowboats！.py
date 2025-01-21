n = int(input())
arr = list()

for i in range(1, n+1):
    if i % 6 == 0:
        arr.append(str(i))
        arr.append('Go!')

    else:
        arr.append(str(i))

if arr[-1] != 'Go!':
    arr.append('Go!')
print(*arr)
