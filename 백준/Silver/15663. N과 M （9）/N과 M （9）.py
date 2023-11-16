# 15663

n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

visited = [False] * n
out = []


def solved(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != li[i]:
            visited[i] = True
            out.append(li[i])
            overlap = li[i]
            solved(depth+1, n, m)
            visited[i] = False
            out.pop()


solved(0, n, m)
