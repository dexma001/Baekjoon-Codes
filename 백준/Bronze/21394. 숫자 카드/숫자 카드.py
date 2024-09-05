n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    temp = sum(arr)
    arr[8] += arr[5]
    arr[5] = 0

    left = list()
    right = list()

    trig = 0

    for i in range(8, -1, -1):
        if arr[i] != 0:
            if trig == 0:
                if arr[i] % 2 == 0:
                    for _ in range((arr[i]//2)):
                        left.append(i+1)
                        right.append(i+1)
                else:
                    for _ in range((arr[i]//2)):
                        left.append(i+1)
                        right.append(i+1)
                    left.append(i+1)
            else:
                if arr[i] % 2 == 0:
                    for _ in range((arr[i]//2)):
                        right.append(i+1)
                        left.append(i+1)
                else:
                    for _ in range((arr[i]//2)):
                        right.append(i+1)
                        left.append(i+1)
                    right.append(i+1)

            trig = (trig + arr[i]) % 2

    print(*(left + right[::-1]))
