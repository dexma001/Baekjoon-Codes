temp = str(input().strip())

small = 0
under = 0
colon = 0

for i in temp:
    if i == ':':
        colon += 1
    elif i == '_':
        under += 1
    else:
        small += 1

print(len(temp) + colon + under * 5)
