for _ in range(int(input())):
    temp = str(input())
    if len(temp) != 7:
        print(0)
        continue

    if temp[0] != temp[2]:
        if temp[0] == temp[1] == temp[4]:
            if temp[2] == temp[3] == temp[5] == temp[6]:
                print(1)
            else:
                print(0)
        else:
            print(0)
    else:
        print(0)
