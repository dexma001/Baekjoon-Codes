import sys
input = sys.stdin.readline
import time

n = int(input())
crane = list(map(int, input().split()))
crane.sort(reverse = True)

m = int(input())
box = list(map(int, input().split()))
box.sort(reverse = True)

if box[0] > crane[0]:
    print(-1)
    quit()
    
answer = 0

while True:
    if not box:
        break
    for i in range(len(crane)):
        for j in range(len(box)):
            if crane[i] >= box[j]:
                del box[j]
                break
    answer += 1
    
print(answer)