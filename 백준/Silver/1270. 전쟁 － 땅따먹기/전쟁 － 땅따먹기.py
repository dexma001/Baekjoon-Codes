import sys
input = sys.stdin.readline
from collections import defaultdict, deque

for _ in range(int(input())):
    arr = deque(list(map(int, input().split())))
    cnt = arr.popleft()
    temp = defaultdict(int)
    for i in arr:
        temp[i] += 1
        
    answer = "SYJKGW"
    
    for i in list(temp.keys()):
        if temp[i] > cnt//2:
            answer = i
            
    print(answer)