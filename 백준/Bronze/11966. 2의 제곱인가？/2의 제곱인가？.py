arr = list()
for i in range(31):
    arr.append(2**i)

n = int(input())
print(1) if n in arr else print(0)