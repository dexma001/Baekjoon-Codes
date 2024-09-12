

submit = []
for i in range(28):
    submit.append(int(input()))
submit.sort()

total = [i+1 for i in range(30)]

for i in range(30):
    try:
        if submit[i] != total[i]:
            print(i+1)
            submit.insert(i, i+1)
    except:
        print(i+1)
