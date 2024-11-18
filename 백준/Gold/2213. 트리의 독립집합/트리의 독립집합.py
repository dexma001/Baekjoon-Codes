# 2213

from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit

n = int(input())
node = [0] + list(map(int, input().split()))

tree = list(list() for _ in range(n+1))
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in tree:
    i.sort()

# 0번째 라인은 고를때 / 1번째 마을은 안고를때
dp = list(list(0 for _ in range(n+1)) for _ in range(2))
visited = list(0 for _ in range(n+1))
use_answer = defaultdict(list)
unuse_answer = defaultdict(list)


def dfs(i):
    visited[i] = 1
    for j in tree[i]:
        if visited[j]:
            continue
        else:
            dfs(j)
            dp[0][i] += dp[1][j]
            use_answer[i].extend(unuse_answer[j])
            dp[1][i] += max(dp[0][j], dp[1][j])
            if dp[0][j] > dp[1][j]:
                unuse_answer[i].extend(use_answer[j])
            else:
                unuse_answer[i].extend(unuse_answer[j])

    dp[0][i] += node[i]
    use_answer[i].append(i)


dfs(1)
print(max(dp[0][1], dp[1][1]))
if dp[0][1] > dp[1][1]:
    use_answer[1].sort()
    print(*use_answer[1])
else:
    unuse_answer[1].sort()
    print(*unuse_answer[1])
