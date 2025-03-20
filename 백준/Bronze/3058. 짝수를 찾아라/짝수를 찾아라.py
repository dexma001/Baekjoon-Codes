#3058

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    sum = 0
    mi = 101
    
    for i in arr:
        if i%2 ==0:
            sum += i
            mi = min(i, mi)

    print(sum, mi)