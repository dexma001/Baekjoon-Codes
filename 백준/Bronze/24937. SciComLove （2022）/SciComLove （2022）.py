temp = 'SciComLove'

n = int(input())
n %= 10

for _ in range(n):
    k = temp[0]
    temp = temp[1:]
    temp += k

print(temp)
