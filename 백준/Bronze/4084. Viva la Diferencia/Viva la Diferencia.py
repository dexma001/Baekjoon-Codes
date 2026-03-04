while True:
    a, b, c, d = map(int, input().split())
    answer = 0
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    
    while a != b or b != c or c != d:
        a1 = abs(a-b)
        b1 = abs(b - c)
        c1 = abs(c - d)
        d1 = abs(d - a)
        
        a = a1
        b = b1
        c = c1
        d = d1
        
        answer += 1
        
    print(answer)
        