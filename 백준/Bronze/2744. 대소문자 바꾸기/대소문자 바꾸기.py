arr = list(map(str, input().rstrip()))
answer = ''

for i in arr:
    if i.isupper() == True:
        answer += i.lower()
    else:
        answer += i.upper()

print(answer)
