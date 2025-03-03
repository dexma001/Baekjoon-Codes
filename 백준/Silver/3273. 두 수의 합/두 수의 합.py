# 3273

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
to_be = int(input())

answer = 0
l = 0
r = n-1

while l != r:
    if arr[l] + arr[r] == to_be:
        answer += 1
        r -= 1

    elif arr[l] + arr[r] > to_be:
        r -= 1

    else:
        l += 1

print(answer)
