n, k = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(float(input()))
    
arr.sort()

answer_1 = 0
answer_2 = 0

for i in range(n):
    if i < k:
        answer_2 += arr[k]
    
    elif i >= n-k:
        answer_2 += arr[n-k-1]
    
    else:
        answer_1 += arr[i]
        answer_2 += arr[i]        
        
answer_1 +=  0.00000001
answer_2 +=  0.00000001

print("{:.2f}".format(answer_1 / (n-k*2), 2))
print("{:.2f}".format(answer_2 / n, 2))
