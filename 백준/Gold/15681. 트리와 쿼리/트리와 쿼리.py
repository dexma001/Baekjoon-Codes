# 15681

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, root, query = map(int, input().split())
node_arr = list([] for _ in range(n+1))
node_cnt = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    node_arr[a].append(b)
    node_arr[b].append(a)
    node_cnt[a] += 1
    node_cnt[b] += 1

answer_arr = [0] * (n+1)
visited = [0] * (n+1)


def dp(i):
    if visited[i] == 1:
        return answer_arr[i]
    else:
        visited[i] = 1
        answer_arr[i] += 1
        for j in node_arr[i]:
            if visited[j] == 0:
                answer_arr[i] += dp(j)
            else:
                continue
        return answer_arr[i]


dp(root)

for _ in range(query):
    print(answer_arr[int(input())])
