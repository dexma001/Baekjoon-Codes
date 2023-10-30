a = str(input())
b = str(input())

len_a = len(a)
len_b = len(b)

li = [[0 for j in range(len(a)+1)] for i in range(len(b)+1)]

for i in range(len(b)):
    for j in range(len(a)):
        if a[j] == b[i]:
            li[i+1][j+1] = li[i][j]+1
        else:
            li[i+1][j+1] = max(li[i][j+1], li[i+1][j])

result = ''
x, y = len(a), len(b)


def str(p, q):
    global result

    if p == 0 or q == 0:
        return result

    elif li[q][p] == li[q][p-1]:
        str(p-1, q)
    elif li[q][p] == li[q-1][p]:
        str(p, q-1)
    else:
        result += a[p-1]
        str(p-1, q-1)


str(x, y)
print(len(result))
