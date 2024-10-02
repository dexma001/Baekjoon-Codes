# 5214

from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())
arr = list([] for _ in range(n+1))
tube = defaultdict(list)

if n == 1:
    print(1)
    quit()

for i in range(m):
    tube[i+1] = list(map(int, input().split()))
    for ii in tube[i+1]:
        arr[ii].append(i+1)

temp = deque([1])
visited = list(0 for _ in range(n+1))
visited[1] = 1
answer = 1
ran = 1

while True:
    for i in range(ran):
        k = temp.popleft()
        ran -= 1

        for ii in arr[k]:
            for iii in tube[ii]:
                if iii == n:
                    print(answer + 1)
                    quit()

                if not visited[iii]:
                    visited[iii] = 1
                    temp.append(iii)
                    ran += 1
    if not temp:
        print(-1)
        quit()
    answer += 1
