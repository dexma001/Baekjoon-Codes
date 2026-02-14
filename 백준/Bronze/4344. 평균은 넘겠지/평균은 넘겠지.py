for _ in range(int(input())):
    arr = list(map(int, input().split()))
    temp = arr.pop(0)
    
    avg = sum(arr) / temp

    avg_over =0
    
    for i in arr:
        if i > avg:
            avg_over += 1
    
    print(f"{avg_over/temp*100:.3f}" + "%")