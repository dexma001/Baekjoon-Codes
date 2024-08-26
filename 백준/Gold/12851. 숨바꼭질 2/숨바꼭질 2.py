# 12851

from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if n >= m:
    print(n-m)
    print(1)

else:
    stack = deque([])
    stack.append(n)
    trig = 1

    answer_arr = list(0 for _ in range(100001))
    answer_cnt = defaultdict(int)
    answer_cnt[n] = 1

    level = 1
    while stack:
        for _ in range(len(stack)):
            temp = stack.popleft()
            if temp == m:
                trig = 0
            else:
                for i in (temp-1, temp+1, temp*2):
                    if 0 <= i <= 100000:
                        if not answer_arr[i]:
                            answer_arr[i] = level
                            stack.append(i)
                            answer_cnt[i] += answer_cnt[temp]
                        else:
                            if answer_arr[i] == level:
                                answer_cnt[i] += answer_cnt[temp]
        level += 1

        if trig == 0:
            print(answer_arr[m])
            print(answer_cnt[m])
            break
