from collections import defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    answer = defaultdict(int)
    for _ in range(int(input())):
        answer[int(input())] += 1
    temp = list(answer.items())
    temp.sort(key=lambda x: (-x[1], x[0]))
    print(temp[0][0])
