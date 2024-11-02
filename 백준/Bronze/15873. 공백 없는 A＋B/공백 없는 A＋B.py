t = str(input().strip())
if len(t) == 4:
    print(20)

elif len(t) == 3:
    if t[1] == '0':
        print(10+int(t[-1]))
    else:
        print(10+int(t[0]))
else:
    print(int(t[0])+int(t[-1]))
