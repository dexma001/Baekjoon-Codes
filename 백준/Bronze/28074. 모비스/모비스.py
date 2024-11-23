arr = list(map(str, input().strip()))
answer = ['M', 'O', 'B', 'S', 'I']
for i in answer:
    if i not in arr:
        print('NO')
        break
else:
    print('YES')
