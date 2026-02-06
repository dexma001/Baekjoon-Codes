import sys
input = sys.stdin.readline

arr = list(0 for _ in range(10000001))

for i in range(1, 10000001):
    if i == 1:
        arr[i] = 5
    elif i == 2:
        arr[i] = 20
    else:
        arr[i] = (arr[i-1] * 5) % 1000000007
        
for _ in range(int(input())):
    print(arr[int(input())])