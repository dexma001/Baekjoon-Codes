answer = ''

for i in input():
    temp = i
    if ord(i) == 32 or 48 <= ord(i) <= 57:
        pass
    else:
        if i.isupper():
            if ord(i)+13 >= 91:
                temp = chr(ord(i)+13-91+65)
            else:
                temp = chr(ord(i)+13)
        else:
            if ord(i) + 13 >= 123:
                temp = chr(ord(i)+13-123+97)
            else:
                temp = chr(ord(i) + 13)

    answer += temp

print(answer)
