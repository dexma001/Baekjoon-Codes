import binascii

for t in range(int(input())):
    n = int(input())
    arr = list(map(str, input().strip()))
    for i in range(len(arr)):
        if arr[i] == "I":
            arr[i] = "1"
        else:
            arr[i] = "0"
    arr = ''.join(arr)
    answer = ''
    for i in range(n):
        answer += chr(int(arr[8*i:8*(i+1)], 2))

    print(f"Case #{t+1}: {answer}")
