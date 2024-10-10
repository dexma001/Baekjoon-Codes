# 8980

import heapq
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
arr = list()
for _ in range(m):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: [x[0], x[1], x[2]])

answer = 0
truck = list()
truck_total = 0
truck_location = 1

while arr:
    i, j, k = arr.pop(0)
    if i > truck_location:
        while truck and truck[0][0] <= i:
            i1, j1 = heapq.heappop(truck)
            answer += j1
            truck_total -= j1

    truck_location = i
    if truck_total + k <= c:
        truck_total += k
        heapq.heappush(truck, [j, k])
    elif truck_total != c:
        temp = c - truck_total
        truck_total = c
        heapq.heappush(truck, [j, temp])
    else:
        temp_loc = 0
        temp_loc_index = -1
        for t in range(len(truck)):
            p, q = truck[t]
            if p > j:
                if p > temp_loc:
                    temp_loc = p
                    temp_loc_index = t
        if temp_loc_index != -1:
            truck[temp_loc_index][1] -= k
            truck.append([j, k])
            heapq.heapify(truck)

while truck:
    ii, jj = heapq.heappop(truck)
    answer += jj

print(answer)
