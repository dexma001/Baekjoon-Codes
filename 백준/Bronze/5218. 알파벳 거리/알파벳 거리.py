n = int(input())

for _ in range(n):
    a, b = list(map(str, input().split()))

    answer = list()

    for i, j in zip(a, b):
        if ord(i) <= ord(j):
            answer.append(str(ord(j)-ord(i)))
        else:
            answer.append(str(ord(j)+26-ord(i)))

    temp = ' '.join(answer)
    print(f"Distances: {temp}")
