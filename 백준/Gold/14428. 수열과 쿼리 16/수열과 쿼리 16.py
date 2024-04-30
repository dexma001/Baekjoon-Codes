# 14428

import sys
import math
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
size = math.ceil(math.log(n, 2) + 1)
segment_tree = list(10**10 for _ in range(2**(size-1)))

arr = list(map(int, input().split()))
for i in range(len(arr)):
    segment_tree.append(arr[i])
segment_tree.extend([10**10] * (2**(size-1) - n))


for i in range(2**(size-1)-1, 0, -1):
    segment_tree[i] = min(segment_tree[i << 1], segment_tree[i << 1 | 1])


def segment_update(idx, diff):
    node = idx + 2**(size-1) - 1
    segment_tree[node] = diff
    while node >> 1 != 0:
        segment_tree[node >> 1] = min(segment_tree[node],
                                      segment_tree[node ^ 1])
        node >>= 1


def segment_search(left, right):
    leftnode = left + 2**(size-1) - 1
    rightnode = right + 2**(size-1) - 1
    answer = 10**10

    while leftnode <= rightnode:
        if leftnode % 2 == 1:
            answer = min(answer, segment_tree[leftnode])
            leftnode += 1
        if rightnode % 2 == 0:
            answer = min(answer, segment_tree[rightnode])
            rightnode -= 1

        leftnode >>= 1
        rightnode >>= 1

    return answer


m = int(input())
for _ in range(m):
    x, y, z = map(int, input().split())
    if x == 1:
        arr[y-1] = z
        segment_update(y, z)
    else:
        a = segment_search(y, z)
        for i in range(y-1, z):
            if arr[i] == a:
                print(i+1)
                break
