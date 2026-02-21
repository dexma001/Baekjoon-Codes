for i in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    
    print(f"Scenario #{i+1}:")
    if arr[2] **2 == arr[1]**2 + arr[0]**2:
        print("yes")
    else:
        print("no")
    print("")