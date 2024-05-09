# 1017

from collections import defaultdict
import sys
import math
input = sys.stdin.readline

n = int(input())
int_arr = list(map(int, input().split()))


def det_prime(i):
    for j in range(2, math.ceil(math.sqrt(i)) + 1):
        if i % j == 0:
            return False
    return True


match_to_make_prime = defaultdict(list)

for i in range(0, n):
    for j in range(0, n):
        bool = det_prime(int_arr[i] + int_arr[j])
        if bool == True:
            match_to_make_prime[i].append(j)


def bimatch(i):
    if visited[i]:
        return False
    visited[i] = True

    for num in match_to_make_prime[i]:
        if num == 0 or num == i:
            continue

        if used[num] == -1 or bimatch(used[num]):
            used[num] = i
            return True
    return False


answer = list()
for i in match_to_make_prime[0]:
    used = [-1] * n
    used[0] = i
    used[i] = 0
    for j in range(0, n):
        if j == 0 | i:
            continue
        else:
            visited = [False] * n
            visited[0] = -1
            visited[i] = -1
            bimatch(j)

    if used.count(-1) == 0:
        answer.append(i)

if len(answer) != 0:
    for i in range(len(answer)):
        answer[i] = int_arr[answer[i]]
    answer.sort()
    print(*answer)
else:
    print('-1')
