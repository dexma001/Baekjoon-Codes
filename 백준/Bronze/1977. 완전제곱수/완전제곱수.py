import math

m = int(input())
n = int(input())

answer = 0
miner = 0
for i in range(m, n+1):
    if math.sqrt(i) == int(math.sqrt(i)):
        answer += i
        if not miner:
            miner = i
            
if answer:
    print(answer)
    print(miner)
else:
    print(-1)