# 3541

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 10**10-1


def binary_search(i, j, p, q):
    if i == j:
        return i

    mid = (i+j)//2
    if mid*p-((n-mid)*q) > 0:
        return binary_search(i, mid, p, q)
    else:
        return binary_search(mid+1, j, p, q)


for _ in range(m):
    u, d = map(int, input().split())
    k = binary_search(0, n, u, d)
    temp_answer = k*u - (n-k)*d
    answer = min(answer, temp_answer)

print(answer)
