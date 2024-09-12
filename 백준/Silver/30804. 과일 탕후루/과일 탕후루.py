# 30804

from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left, right, cnt = 0, 0, 0
fruits = defaultdict(int)
answer = 0

while right < n:
    if fruits[arr[right]] == 0:
        cnt += 1
    fruits[arr[right]] += 1

    while cnt > 2:
        fruits[arr[left]] -= 1
        if fruits[arr[left]] == 0:
            cnt -= 1
        left += 1

    answer = max(answer, right-left+1)
    right += 1

print(answer)
