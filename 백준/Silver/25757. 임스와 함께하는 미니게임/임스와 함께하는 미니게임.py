# 25757

from collections import defaultdict
import sys
input = sys.stdin.readline

n, game = input().split()
game_dict = {'Y': 1, 'F': 2, 'O': 3}
n = int(n)

arr = list()
dup = defaultdict(int)

for _ in range(n):
    temp = str(input().rstrip())
    if dup[temp] == 0:
        arr.append(temp)
        dup[temp] = 1

print(len(arr)//game_dict[game])
