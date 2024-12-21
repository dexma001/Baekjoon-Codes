arr = {'k': 0, 'l': 0, 'p': 0}
for _ in range(3):
    a = str(input())
    if a[0] in arr.keys():
        arr[a[0]] += 1

if arr['k'] != 0 and arr['l'] != 0 and arr['p'] != 0:
    print('GLOBAL')
else:
    print('PONIX')
