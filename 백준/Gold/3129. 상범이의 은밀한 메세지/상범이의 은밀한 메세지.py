code = str(input().strip())
temp = str(input().strip())

code_len = len(code)
temp_len = len(temp)

t_key = ''

for i in range(code_len - temp_len+1):
    if t_key != '':
        break
    t = ''
    for j in range(i, i + temp_len):
        a = ord(code[j])-97
        b = ord(temp[j-i])-97
        
        if a <= b:
            t += chr(b-a + 97)    
        elif a > b:
            t += chr(26 - a + b + 97)
    
    for i in range(1, len(t)//2+1):
        tt = t[:i]
        ttt = ''
        for i in range(len(t)//len(tt)):
            ttt += tt
        ttt += tt[:len(t) - len(ttt)] 
        if ttt == t:
            t_key = tt    
    
key_len = len(t_key)

for t in range(key_len):
    key = t_key[-t:] + t_key[:-t]
    temp_key = ''

    for i in range(code_len//key_len):
        temp_key += key
        
    temp_key += key[:code_len - len(temp_key)]

    answer = ''

    for i in range(code_len):
        answer += chr((ord(code[i])-97 + ord(temp_key[i])-97)%26 + 97)
        
    if temp in answer:
        print(answer)
        quit()