import sys
input = sys.stdin.readline

n = int(input())

li = list(map(int, input().split()))
maxans = li
minans = li

for i in range(n-1):
    li = list(map(int, input().split()))
    maxans = [li[0] + max(maxans[0], maxans[1]), li[1] +
              max(maxans), li[2]+max(maxans[1], maxans[2])]
    minans = [li[0] + min(minans[0], minans[1]), li[1] +
              min(minans), li[2]+min(minans[1], minans[2])]

print(max(maxans), min(minans))
