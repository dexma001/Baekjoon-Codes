n, k = map(int, input().split())
arr = list(map(str, input().strip()))

answer =0

for i in range(n):
    if arr[i] == "P":
        for j in range(-k, k+1):
            if j == 0:
                continue
            if 0<= i+j < n and arr[i+j] == "H":
                answer += 1
                arr[i+j] = "O"
                break
        
    else:
        continue
    
print(answer)