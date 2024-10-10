# 8980

import heapq
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
arr = list()
for _ in range(m):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: [x[0], x[1], -x[2]])

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
    if not truck:
        heapq.heappush(truck, [j, min(c, k)])
        truck_total = min(c, k)
    elif truck_total + k <= c:
        truck_total += k
        heapq.heappush(truck, [j, k])
    else:  # truck_total + k > c
        truck.sort(key=lambda x: [x[0], -x[1]])
        if truck[-1][0] <= j and c - truck_total > 0:
            truck.append([j, c - truck_total])
            truck_total = c
        else:
            while truck and truck[-1][0] > j:
                if c-(truck_total-truck[-1][1]) == k:
                    truck.pop()
                    truck.append([j, k])
                    truck_total = c
                    break
                elif c - (truck_total - truck[-1][1]) > k:
                    break
                else:
                    truck_total -= truck[-1][1]
                    truck.pop()

            if truck_total <= c:
                if truck and truck[-1][0] > j:
                    truck[-1][1] = c-(truck_total-truck[-1][1]+k)
                    truck.append([j, k])
                    truck_total = c
                else:
                    truck.append([j, min(c - truck_total, k)])
                    truck_total = c
        heapq.heapify(truck)

while truck:
    ii, jj = heapq.heappop(truck)
    answer += jj

print(answer)

'''
좋은 반례
5 40
3
1 5 10
2 4 40
4 5 40
answer = 80

4 50
4
1 3 15
1 4 35
2 3 90
3 4 80
answer = 100

4 50
4
1 3 35
1 4 90
2 3 10
3 4 30
answer = 80

4 50
4
1 3 35
1 4 10
2 3 10
3 4 30
answer = 80
'''
