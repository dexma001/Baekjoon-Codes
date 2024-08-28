arr = list(map(int, input().split()))
num = [100, 100, 200, 200, 300, 300, 400, 400, 500]

if sum(arr) >= 100:
    for i in range(9):
        if arr[i] > num[i]:
            print('hacker')
            break
    else:
        print('draw')
else:
    print('none')
