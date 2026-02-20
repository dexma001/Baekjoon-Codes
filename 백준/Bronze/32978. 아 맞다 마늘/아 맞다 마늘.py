n = int(input())
arr = list(map(str, input().split()))
ans = list(map(str, input().split()))
for i in ans:
    arr.remove(i)
print(*arr)