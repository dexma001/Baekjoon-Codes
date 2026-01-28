for _ in range(int(input())):
    n = int(input())
    temp = n + int(str(n)[::-1])
    
    if temp == int(str(temp)[::-1]):
        print("YES")
    else:
        print("NO")