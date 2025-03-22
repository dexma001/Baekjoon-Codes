import itertools

n = int(input())
arr = list(i for i in range(1, n+1))

answer = list(itertools.permutations(arr))
for i in answer:
    print(*i)