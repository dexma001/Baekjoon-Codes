import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list()
    for _ in range(n):
        arr.append(list(map(int, input().split())))
        
    arr.sort(key=lambda x: [x[0], x[1]])

    answer = 1
    mini = arr[0][1]
    for i in range(1, n):
        
        if arr[i][1] < mini:
            mini = arr[i][1]
            answer += 1
        else:
            continue
    print(answer)