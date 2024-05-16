# 9655

def baskin(i):
    k = i % 2
    if k >= 4:
        baskin(k)
    else:
        if k == 1 or k == 3:
            return 'SK'
        else:
            return 'CY'


print(baskin(int(input())))
