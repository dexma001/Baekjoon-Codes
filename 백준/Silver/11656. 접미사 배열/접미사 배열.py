n = str(input())
n_len = len(n)

arr = list()

for i in range(n_len):
    arr.append(n[i:])

arr.sort()
for i in arr:
    print(i)