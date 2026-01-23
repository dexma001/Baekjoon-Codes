import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, n = map(int, input().split())
    
    if n % 2 == 0:
        print((a*(n//2) + b*(n//2))**2)
    else:
        miner = n//2
        major = n//2 + 1
        
        print((a*miner + b*major) * (a*major + b*miner))