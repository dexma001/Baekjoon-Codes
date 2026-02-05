n = int(input())
arr = dict()

for _ in range(n):
    a, b = map(int, input().split())
    arr[a] = b
    
r = int(input())

for _ in range(r):
    temp = list(map(int, input().split()))
    temp = temp[1:]
    answer = list()
    
    for i in temp:
        try:
            answer.append(arr[i])
        except:
            print("YOU DIED")
            break
    else:
        print(*answer)
