import heapq

arr = list()

for _ in range(int(input())):
    heapq.heappush(arr, int(input()))
    
while arr:
    print(heapq.heappop(arr))