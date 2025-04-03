# 10451

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

t = int(input())


def permutation(nn, temp):
    if nn in temp:
        return temp

    temp.append(nn)
    return permutation(arr[nn], temp)


for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    answer = 0
    visited = list(0 for _ in range(n+1))
    for i in range(1, n+1):
        if not visited[i]:
            cycle = permutation(i, list())
            for node in cycle:
                visited[node] = 1
            answer += 1

        else:
            continue
    print(answer)
