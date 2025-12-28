import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b = map(int, input().split())

arr = list()

for i in range(n):
    arr.append(list())
    if i == a:
        for j in range(m):
            if j <= b:
                arr[-1].append('E')
            else:
                arr[-1].append('W')
    else:
        if i < a:
            for j in range(m):
                arr[-1].append("S")
        else:
            for j in range(m):
                arr[-1].append("N")
                
for i in arr:
    print(''.join(i))