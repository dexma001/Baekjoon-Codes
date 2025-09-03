# 1027

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(float, input().split()))

if len(arr) <= 3:
    print(len(arr) - 1)

else:
    answer = 0

    for i in range(n):
        temp_answer = 0
        for j in range(0, i):
            for k in range(j+1, i):
                if arr[i] >= arr[j] and arr[j] + (((arr[i] - arr[j]) / (i-j)) * (k-j)) <= arr[k]:
                    break
                elif arr[i] < arr[j] and arr[i] + (((arr[j] - arr[i]) / (i-j)) * (i-k)) <= arr[k]:
                    break
                else:
                    continue
            else:
                temp_answer += 1

        for j in range(i+1, n):
            for k in range(i+1, j):
                if arr[i] >= arr[j] and arr[j] + (((arr[i] - arr[j]) / (j-i)) * (j-k)) <= arr[k]:
                    break
                elif arr[i] < arr[j] and arr[i] + (((arr[j] - arr[i]) / (j-i)) * (k-i)) <= arr[k]:
                    break
                else:
                    continue
            else:
                temp_answer += 1

        answer = max(answer, temp_answer)

    print(answer)
