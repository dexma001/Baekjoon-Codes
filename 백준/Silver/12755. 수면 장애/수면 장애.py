n = int(input())

max = 9

if n < 10:
    print(n)
else:
    j = 1
    i = 2
    prev = 9
    while True:
        max += 9*(10**j)*i
        if prev < n and max >= n:
            break
        i += 1
        j += 1
        prev = max

    cnt = (n - (prev+1))//i
    num = (10**(i-1)) + cnt
    num = str(num)
    d = (n - (prev+1)) % i
    print(num[d])
