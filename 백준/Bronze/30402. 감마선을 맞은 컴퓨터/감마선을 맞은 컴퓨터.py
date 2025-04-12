# 30402

import sys
input = sys.stdin.readline

arr = {'w': 0, 'b': 0, 'g': 0}

for _ in range(15):
    temp = list(map(str, input().split()))
    if 'w' in temp:
        arr['w'] += 1

    if 'b' in temp:
        arr['b'] += 1

    if 'g' in temp:
        arr['g'] += 1

if arr['w']:
    print('chunbae')
elif arr['b']:
    print('nabi')
else:
    print('yeongcheol')
