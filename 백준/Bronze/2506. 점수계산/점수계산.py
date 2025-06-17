n = int(input())
arr = list(map(int, input().split()))

answer = 0
temp_answer = 0

for i in arr:
    if i == 0:
        temp_answer =0
    else:
        temp_answer += 1
        answer += temp_answer
    
print(answer)