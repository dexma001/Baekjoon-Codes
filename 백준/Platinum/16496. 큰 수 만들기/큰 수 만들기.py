# 16496

import functools

n = int(input())
arr = list(map(str, input().split()))

arr.sort(key=functools.cmp_to_key(
    lambda x, y: int(x+y) - int(y+x)), reverse=True)

answer = ''.join(arr).lstrip('0')
print(answer or 0)
