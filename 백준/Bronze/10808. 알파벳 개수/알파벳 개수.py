arr = list(0 for _ in range(26))

q = list(map(str, input().rstrip()))
for i in q:
    arr[ord(i) - 97] += 1

print(*arr)
