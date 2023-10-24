import sys

n = int(input())

if n == 1:
    li = list(map(int, sys.stdin.readline().split()))
    print(sum(li) - max(li))


else:
    a = ((n-2)**2)*5 + ((n-2) * 4)
    b = 4
    c = 5*(n**2) - a - b*3

    atof = dict()
    ch = 97
    li = list(map(int, sys.stdin.readline().split()))
    for i in range(6):
        atof[chr(ch)] = li[i]
        ch += 1

    atof_v = list(atof.values())

    x = a * min(atof.values())
    y = b * (min(atof['a'], atof['f']) + min(atof['b']+atof['c'],
                                             atof['c']+atof['e'], atof['d']+atof['e'], atof['d']+atof['b']))
    s_2 = []
    for i in range(0, 5):
        for j in range(i+1, 6):
            s_2.append(atof_v[i]+atof_v[j])
    s_2.remove(atof_v[0]+atof_v[5])
    s_2.remove(atof_v[1]+atof_v[4])
    s_2.remove(atof_v[2]+atof_v[3])
    z = c/2 * min(s_2)

    print(int(x+y+z))
