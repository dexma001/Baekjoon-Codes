n = int(input())
arr = list(int(input()) for _ in range(n))

answer = 0
for i in range(int(input())):
    answer += arr[int(input())-1]
print(answer)
