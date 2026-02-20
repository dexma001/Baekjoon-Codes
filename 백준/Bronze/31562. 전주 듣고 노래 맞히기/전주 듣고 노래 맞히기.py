from collections import defaultdict

n, m = map(int, input().split())
arr = defaultdict(list)

for _ in range(n):
    temp = list(map(str, input().split()))
    temp.pop(0)
    arr[''.join(temp[1:4])].append(temp[0])
    
for _ in range(m):
    temp = arr[''.join(list(map(str, input().split())))]
    if len(temp) >= 2:
        print("?")
    elif len(temp) == 0:
        print("!")
    else:
        print(*temp)