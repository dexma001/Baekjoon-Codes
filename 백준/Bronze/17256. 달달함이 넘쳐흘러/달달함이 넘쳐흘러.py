import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
result = list(map(int, input().split()))

answer = list()

answer.append(result[0] - arr[2])
answer.append(result[1]//arr[1])
answer.append(result[2] - arr[0])

print(*answer)
