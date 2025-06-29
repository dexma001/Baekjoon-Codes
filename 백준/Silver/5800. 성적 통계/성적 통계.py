for i in range(int(input())):
    arr = list(map(int, input().split()))
    arr.pop(0)
    arr.sort()
    gap = 0
    for j in range(len(arr) - 1):
       gap = max(gap, abs(arr[j] - arr[j+1])) 
    print(f"Class {i+1}")
    print(f"Max {max(arr)}, Min {min(arr)}, Largest gap {gap}")
    