arr = [0, 0, 0, 0, 0]
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 0 or b == 0:
        arr[4] += 1
    else:
        if a >= 0:
            if b >= 0:
                arr[0] += 1
            else:
                arr[3] += 1
        else:
            if b >= 0:
                arr[1] += 1
            else:
                arr[2] += 1

for i in range(1, 5):
    print(f"Q{i}: {arr[i-1]}")
print(f"AXIS: {arr[-1]}")