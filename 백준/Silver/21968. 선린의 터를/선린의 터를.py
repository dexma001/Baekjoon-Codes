for _ in range(int(input())):
    n = list(int(i) for i in bin(int(input()))[2:])
    n.reverse()

    answer = 0
    mark = 0

    for i in n:
        if i:
            answer += 3**mark
        mark += 1

    print(answer)
