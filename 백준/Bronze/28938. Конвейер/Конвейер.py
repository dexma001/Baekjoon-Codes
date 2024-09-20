n = int(input())
arr = sum(list(map(int, input().split())))
if arr < 0:
    print('Left')
elif arr > 0:
    print('Right')
else:
    print('Stay')
