case = int(input())
for i in range(case):
    n = int(input())
    if n == 0:
        print('Case #{0}: INSOMNIA'.format(i+1))
        continue

    temp_set = set(list(map(int, str(n))))
    j = 1
    while len(temp_set) < 10:
        j += 1
        temp = int(n * j)
        temp_set_ = list(map(int, str(temp)))
        temp_set.update(temp_set_)

    print('Case #{0}: {1}'.format(i+1, n*j))
