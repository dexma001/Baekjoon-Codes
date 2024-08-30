# 16946

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))

all_hollow = list(list(0 for _ in range(m)) for _ in range(n))
hollow_group = defaultdict(int)
hollow_group_num = 1

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 or all_hollow[i][j] != 0:
            continue
        else:
            group = defaultdict(int)
            group_len = 0

            stack = deque([])
            stack.append([i, j])
            group[i, j] = 1
            group_len += 1

            while stack:
                a, b = stack.popleft()
                for k in range(4):
                    y = a + dy[k]
                    x = b + dx[k]
                    if 0 <= y < n and 0 <= x < m and arr[y][x] == 0 and not group[(y, x)]:
                        group[y, x] = 1
                        stack.append([y, x])
                        group_len += 1

            for p, q in list(group):
                all_hollow[p][q] = group_len
                hollow_group[p, q] = hollow_group_num

            hollow_group_num += 1


for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            temp = defaultdict(int)
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if 0 <= y < n and 0 <= x < m and arr[y][x] == 0:
                    if not temp[hollow_group[y, x]]:
                        temp[hollow_group[y, x]] = 1
                        arr[i][j] = (arr[i][j] + all_hollow[y][x]) % 10

for i in arr:
    print(*i, sep='')
