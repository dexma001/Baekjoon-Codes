from collections import deque

for _ in range(int(input())):
    n = int(input())
    arr = list(map(str, input().split()))

    answer = deque([])
    answer.append(arr[0])

    for i in range(1, n):
        temp = arr[i]
        if ord(temp) <= ord(answer[0]):
            answer.appendleft(temp)
        else:
            answer.append(temp)

    print("".join(answer))
