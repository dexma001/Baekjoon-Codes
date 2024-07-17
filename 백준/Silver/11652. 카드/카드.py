# 11652

from collections import defaultdict
import sys
input = sys.stdin.readline

temp = defaultdict(int)

for _ in range(int(input())):
    temp[int(input())] -= 1

temp_item = list(temp.items())
temp_item.sort(key=lambda x: [x[1], x[0]])

print(temp_item[0][0])
