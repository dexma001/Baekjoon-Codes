import sys
input = sys.stdin.readline
from collections import defaultdict

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    cnt = arr.pop(0)
    temp = defaultdict(int)
    for i in arr:
        temp[i] += 1
        
    answer = "SYJKGW"
    
    for i in list(temp.keys()):
        if temp[i] > cnt//2:
            answer = i
            
    print(answer)