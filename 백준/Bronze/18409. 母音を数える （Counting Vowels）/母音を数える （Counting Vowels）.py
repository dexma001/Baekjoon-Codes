n = int(input())
arr = list(map(str, input().rstrip()))

temp = ['a', 'e', 'i', 'o', 'u']

answer = 0
for i in arr:
    if i in temp:
        answer += 1

print(answer)
