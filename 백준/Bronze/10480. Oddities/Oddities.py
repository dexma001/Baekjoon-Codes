for _ in range(int(input())):
    temp = int(input())
    if abs(temp) %2 == 0:
        print(f"{temp} is even")
    else:
        print(f"{temp} is odd")