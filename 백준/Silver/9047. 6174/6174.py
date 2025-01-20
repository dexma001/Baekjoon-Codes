for _ in range(int(input())):
    arr = list(k for k in str(input()))
    
    answer = 0
    while True:
        arr_sum = int(''.join(arr))
        
        if arr_sum == 6174:
            print(answer)
            break
        
        arr.sort()
        temp1 = int(''.join(arr))
        temp2 = 0
        for i in range(4):
            if arr[i] != '0':
                temp2 += int(arr[i]) * (10**(i))
        arr = list(j for j in str(temp2 - temp1))
        while len(arr) != 4:
            arr.insert(0, '0')
            
        answer += 1
            

            