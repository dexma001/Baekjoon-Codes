for _ in range(int(input())):
    x = int(input())
    ans = 0
    if (x%2) == 0:
        ans += x//2
    else:
        ans += x//2 + 1
        
    if (x%6 == 0 or x % 6 == 4):
        ans += x//3
    else:
        ans += x//3 + 1
        
    print(ans)