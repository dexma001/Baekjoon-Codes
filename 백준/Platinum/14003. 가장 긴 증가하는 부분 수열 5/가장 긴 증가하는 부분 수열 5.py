import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))


# 이진탐색부분은 인터넷 참고함
def binary_search(start, end, target):
    if start > end:
        return start

    mid = (start+end)//2

    if lis[mid] > target:
        return binary_search(start, mid-1, target)
    elif lis[mid] == target:
        return mid
    else:
        return binary_search(mid+1, end, target)


dp = list()
dp.append([0, arr[0]])
lis = list([arr[0]])


for i in range(1, n):
    if arr[i] > lis[-1]:
        lis.append(arr[i])
        dp.append([len(lis)-1, arr[i]])
    else:
        idx = binary_search(0, len(lis)-1, arr[i])
        lis[idx] = arr[i]
        dp.append([idx, arr[i]])

print(len(lis))
last_idx = len(lis)-1
res = []
for i in range(len(dp)-1, -1, -1):
    if dp[i][0] == last_idx:
        res.append(dp[i][1])
        last_idx -= 1

res.reverse()
print(*res)
