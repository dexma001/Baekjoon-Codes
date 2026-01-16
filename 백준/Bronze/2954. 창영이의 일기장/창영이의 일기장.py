temp = list(map(str, input().strip()))
temp = temp[::-1]

answer = list()

mo = ['a', 'e', 'i', 'o', 'u']

while temp:
    i = temp.pop()
    answer.append(i)
    
    if i in mo:
        for _ in range(2):
            temp.pop()
    
print(''.join(answer))