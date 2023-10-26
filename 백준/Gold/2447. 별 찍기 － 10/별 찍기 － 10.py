import copy

n = int(input())
n1 = copy.deepcopy(n)
li = [['*' for x in range(n)] for y in range(n)]
m = 0

while n != 1:
    n = n / 3
    m += 1

for i in range(m, 0, -1):
    per = int(3**i)
    space = int(3**(i-1))
    for j in range(space, n1, per):
        for k in range(space, n1, per):
            for p in range(j, j+space):
                for q in range(k, k+space):
                    li[p][q] = ' '

for i in range(len(li)):
    print(''.join(li[i])) #' '.join(li[i])가 더 맛도리임
