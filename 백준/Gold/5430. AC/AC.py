import sys
from collections import deque

cnt = int(input())


for i in range(cnt):
    cmd = sys.stdin.readline().strip()
    n = int(input())
    li = deque(sys.stdin.readline().strip()[1:-1].split(','))

    cnt1 = 0
    if n == 0:
        li = []
    for i in cmd:
        if i == 'R':
            cnt1 += 1
        else:
            if len(li) == 0:
                print('error')
                break
            else:
                if cnt1 % 2 == 0:
                    li.popleft()
                else:
                    li.pop()
    else:
        if cnt1 % 2 == 0:
            print("[" + ','.join(li)+"]")
        else:
            li.reverse()
            print("[" + ','.join(li)+"]")
