# 1812

n = int(input())
arr = list(int(input()) for _ in range(n))
sum_c = sum(arr) // 2

k = 0
for i in range(0, n-1, 2):
    k += (arr[i+1] - arr[i])

answer = list()
answer.append((arr[-1] - k)//2)

for i in range(n-1):
    answer.append(arr[i] - answer[-1])

for i in answer:
    print(i)
