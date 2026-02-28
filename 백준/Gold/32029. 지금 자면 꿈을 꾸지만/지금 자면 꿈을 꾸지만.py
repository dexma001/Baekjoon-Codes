import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

tot = 0

for i in range(n+1):
    for x in range(a):
        cur_time = 0
        count = 0
        
        for j in range(i):
            if cur_time + a <= arr[j]:
                cur_time += a
                count += 1

        cur_time += (b * x)
        
        for j in range(i, n):
            if cur_time + a - x <= arr[j]:
                cur_time += a - x
                count += 1
        
        tot = max(tot, count)
    
print(tot)