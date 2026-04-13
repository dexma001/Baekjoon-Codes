#17095

n = int(input())
arr = list(map(int, input().split()))

maxim = max(arr)
minim = min(arr)

maxim_idx = -1
minim_idx = -1

temp_answer = 10e5 + 1

for i in range(n):
    if arr[i] == maxim:
        maxim_idx = i
    
    if arr[i] == minim:
        minim_idx = i

    if maxim_idx >= 0 and minim_idx >= 0:
        temp_answer = min(temp_answer, abs(maxim_idx - minim_idx) + 1)

print(temp_answer)