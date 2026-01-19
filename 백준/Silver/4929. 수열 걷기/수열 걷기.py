import sys
input = sys.stdin.readline
from collections import deque, defaultdict

while True:
    arr1 = deque(list(map(int, input().split())))

    if arr1[0] == 0:
        quit()

    arr1_len = arr1.popleft()
    arr2 = deque(list(map(int, input().split())))
    arr2_len = arr2.popleft()

    answer = 0

    temp_arr1 = 0
    temp_arr2 = 0
    
    while arr1 and arr2:
        if arr1[0] > arr2[0]:
            temp_arr2 += arr2.popleft()
        elif arr1[0] < arr2[0]:
            temp_arr1 += arr1.popleft()
        else:
            answer += max(temp_arr1, temp_arr2) + arr1[0]
            arr1.popleft()
            arr2.popleft()
            temp_arr1 = temp_arr2 = 0
    
    while arr1:
        temp_arr1 += arr1.popleft()
    
    while arr2:
        temp_arr2 += arr2.popleft()

    answer += max(temp_arr1, temp_arr2)

    print(answer)
