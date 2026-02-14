n, l = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

answer = 0
start = 0

for i in arr:
    if not start:
        start = i
    else:
        if i - start >= l:
            answer += 1
            start = i

answer += 1
print(answer)