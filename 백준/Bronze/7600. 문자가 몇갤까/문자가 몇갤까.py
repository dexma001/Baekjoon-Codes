while True:
    temp = list(map(str, input().strip()))
    if len(temp) == 1 and temp[0] == "#":
        break
    
    arr = list()
    for i in temp:
        if i.isalpha():
            i = i.lower()
            if i not in arr:
                arr.append(i)

    print(len(arr))