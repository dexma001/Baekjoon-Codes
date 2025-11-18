import sys
input = sys.stdin.readline
answer_sum = 0
answer_xor = 0

for _ in range(int(input())):
    temp = list(map(int, input().split()))

    if temp[0] == 1:
        answer_sum += temp[1]
        answer_xor ^= temp[1]
    elif temp[0] == 2:
        answer_sum -= temp[1]
        answer_xor ^= temp[1]
    elif temp[0] == 3:
        print(answer_sum)
    else:
        print(answer_xor)