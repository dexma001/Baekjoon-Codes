# idea from https://hijkl2e.tistory.com/119

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    leng = int(input())
    arr = list(map(int, input().split()))
    all_sum = sum(arr)

    if leng < 3:
        print(max(arr))
        continue

    temp = list()
    i = 2
    temp.append(arr[0])
    temp.append(arr[1])

    while i < leng:
        if len(temp) < 2:
            temp.append(arr[i])
            i += 1
            continue

        if temp[-1] >= max(arr[i], temp[-2]):
            t1 = temp.pop()
            t2 = temp.pop()
            arr[i] = arr[i] + t2 - t1

        else:
            temp.append(arr[i])
            i += 1

    l_r = [0, 0]
    turn = 0

    left = 0
    right = len(temp)-1

    while left <= right:
        if temp[left] > temp[right]:
            l_r[turn] += temp[left]
            left += 1
        elif temp[left] < temp[right]:
            l_r[turn] += temp[right]
            right -= 1
        else:
            if right - left <= 2:
                l_r[turn] += temp[left]
                left += 1
            else:
                if temp[left+1] <= temp[right-1]:
                    l_r[turn] += temp[left]
                    left += 1
                else:
                    l_r[turn] += temp[right]
                    right -= 1

        turn ^= 1

    print((all_sum+(l_r[0]-l_r[1]))//2)
