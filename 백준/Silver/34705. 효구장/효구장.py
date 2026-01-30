from itertools import combinations
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    
    answer = 0
    for i in range(1, 6):
        if answer == 1:
            break
        temp = list(combinations(arr, i))
        for j in temp:
            if x<= sum(j) and sum(j) <= y:
                answer = 1
                break
            
    print("YES") if answer else print("NO")