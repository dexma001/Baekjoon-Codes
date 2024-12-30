# 1256

import math
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
total = math.comb(n+m, max(n, m))

if total < k:
    print(-1)
    quit()

answer = ''


def dfs(a, z, num):
    global answer
    if a == 0 and z == 0:
        return

    elif num == k:
        answer += 'a'*a
        answer += 'z'*z
        return
    else:
        if num + math.comb(a+z-1, max(a-1, z)) > k:
            answer += 'a'
            return dfs(a-1, z, num)
        else:
            answer += 'z'
            return dfs(a, z-1, num + math.comb(a+z-1, max(a-1, z)))


if math.comb(n+m-1, max(n-1, m)) >= k:
    answer += 'a'
    dfs(n-1, m, 1)
else:
    answer += 'z'
    dfs(n, m-1, 1+math.comb(n+m-1, max(n-1, m)))

print(answer)
