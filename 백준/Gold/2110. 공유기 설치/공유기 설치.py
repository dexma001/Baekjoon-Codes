#2110

import sys
input = sys.stdin.readline

n, c = map(int, input().split())

arr = list()
for _ in range(n):
    arr.append(int(input()))
    
arr.sort()
start = 1
end = arr[-1] - arr[0]

while start<= end:
    mid = (start+end)//2
    cnt = 1
    cur_rout = arr[0]
    
    for i in range(1, n):
        if arr[i] >= cur_rout + mid:
            cnt += 1
            cur_rout = arr[i]
            
    if cnt >= c:
        start = mid+1
    else:
        end = mid-1
        
print(end)