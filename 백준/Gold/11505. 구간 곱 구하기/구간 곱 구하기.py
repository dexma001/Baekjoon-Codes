# 11505

import sys
import math
input = sys.stdin.readline

n, m, k = map(int, input().split())

size = math.ceil(math.log(n, 2) + 1)
tree = [1] * (2**(size))
for i in range(n):
    tree[i+2**(size-1)] = int(input())

for i in range(2**(size-1)-1, 0, -1):
    tree[i] = (tree[i << 1] * tree[i << 1 | 1]) % 1000000007


def segment_update(idx, diff):
    node = idx + 2**(size-1) - 1
    tree[node] = diff
    while node >> 1 != 0:
        tree[node >> 1] = (tree[node] * tree[node ^ 1]) % 1000000007
        node >>= 1


def segment_search(left, right):
    leftnode = left + (2**(size-1)) - 1
    rightnode = right + (2**(size-1)) - 1
    answer = 1

    while leftnode <= rightnode:
        if leftnode == rightnode:
            answer *= (tree[leftnode] % 1000000007)
            break
        if leftnode % 2 == 1:
            answer *= (tree[leftnode] % 1000000007)
            leftnode += 1
        if rightnode % 2 == 0:
            answer *= (tree[rightnode] % 1000000007)
            rightnode -= 1

        leftnode >>= 1
        rightnode >>= 1

    return answer


for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        segment_update(b, c)
    else:
        print(segment_search(b, c) % 1000000007)
