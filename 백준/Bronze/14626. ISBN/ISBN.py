arr = list(map(str, input().strip()))
weight = 0
value = 1

for i in range(13):
    if arr[i] == '*':
        if i % 2 == 0:
            continue
        else:
            value = 3
            continue
    
    if i % 2 == 0:
        weight += int(arr[i])
    else:
        weight += int(arr[i]) * 3

for i in range(0, 10):
    if 0 == (weight + value * i )%10:
        print(i)
        break