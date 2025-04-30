temp = str(input().strip())
if temp[0] != '"' or temp[-1] != '"' or len(temp) < 3:
    print('CE')
else:
    print(temp[1:-1])
