import sys
input = sys.stdin.readline
from collections import defaultdict
import math

n, m, k = map(int, input().split())
arr = list()

for j in range(m):
	temp = list(map(float, input().split()))
	for i in range(n):
		arr.append([j, temp[i*2], temp[i*2+1]])

arr.sort(key=lambda x:-x[2])

answer = 0
count = defaultdict(int)
cnt = 0

for i in range(m*n):
	if cnt == k:
		break
	if count[arr[i][1]]:
		continue
	else:
		count[arr[i][1]] = 1
		cnt += 1
		answer += arr[i][2]

print(round(answer, 1))

