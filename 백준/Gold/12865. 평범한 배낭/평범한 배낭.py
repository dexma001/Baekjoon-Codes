#12865

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
weight_list = list(0 for _ in range(k+1))

item_list = list() #weight, value
for _ in range(n):
    item_list.append(list(map(int, input().split())))
    
item_list.sort()  
    
for weight, value in item_list:
    if weight > k:
        continue
    for i in range(k, 0, -1):
        if weight_list[i] and i+weight <= k:
            weight_list[i+weight] = max(weight_list[i+weight], weight_list[i] + value)
    
    weight_list[weight] = max(weight_list[weight], value)
        
print(max(weight_list))