for _ in range(int(input())):
    j, n = map(int,  input().split())
    arr = list()
    for _ in range(n):
        a,b = map(int, input().split())
        arr.append(a*b)
    arr.sort(reverse = True)
    answer = 0
    for i in arr:
        if j > 0:
            j -= i
            answer += 1
    print(answer)