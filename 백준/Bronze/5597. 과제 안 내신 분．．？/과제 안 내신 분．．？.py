import sys
input = sys.stdin.readline

arr = list(i+1 for i in range(30))

for _ in range(28):
    arr.remove(int(input()))

for i in arr:
    print(i)
