n = int(input())
arr = list(map(float, input().split()))

answer = 0
temp_answer = False
for i in arr:
    if i % 1 != 0 and not answer:
        answer += 1
    answer += int(i)

print(answer)
