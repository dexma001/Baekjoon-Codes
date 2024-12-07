from collections import defaultdict

arr1 = list(map(str, input().strip()))
arr2 = list(map(str, input().strip()))

dic1 = defaultdict(int)
dic2 = defaultdict(int)

for i in arr1:
    dic1[i] += 1
for j in arr2:
    dic2[j] += 1


test = 'abcdefghijklmnopqrstuvwxyz'

answer = 0
for i in test:
    if dic1[i]:
        if dic2[i]:
            answer += (max(dic1[i], dic2[i]) - min(dic1[i], dic2[i]))
        else:
            answer += dic1[i]
    elif not dic1[i]:
        if dic2[i]:
            answer += dic2[i]
        else:
            continue
    else:
        continue
print(answer)
