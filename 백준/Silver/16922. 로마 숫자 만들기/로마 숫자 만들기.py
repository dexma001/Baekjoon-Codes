from itertools import combinations_with_replacement

arr = [1, 5, 10, 50]
answer = list()

for i in combinations_with_replacement(arr, int(input())):
    answer.append(sum(i))

print(len(set(answer)))
