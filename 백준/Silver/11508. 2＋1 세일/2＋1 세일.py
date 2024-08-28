# 11508

arr = list(int(input()) for _ in range(int(input())))
arr.sort()

answer = 0
while len(arr) >= 3:
    a = arr.pop()
    b = arr.pop()
    c = arr.pop()
    answer += (a+b)

answer += sum(arr)
print(answer)
