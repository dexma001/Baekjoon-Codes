# 4659

import sys
input = sys.stdin.readline

vowel_list = ['a', 'e', 'i', 'o', 'u']
prev_except = ['e', 'o']

while True:
    temp = str(input().strip())
    if temp == 'end':
        break

    arr = list(i for i in temp)

    accep = 1  # 옳은지
    is_vowel = 0
    vowel = 0  # 모음 연속
    constant = 0  # 자음 연속
    prev = ''  # 바로 전 문자

    for i in arr:
        if not accep:
            break

        if not prev:
            prev = i
            if i in vowel_list:
                is_vowel += 1
                vowel += 1
            else:
                constant += 1

        else:
            if i == prev:
                if i not in prev_except:
                    accep = 0

            if i in vowel_list:
                is_vowel += 1
                constant = 0
                vowel += 1
            else:
                vowel = 0
                constant += 1

            if vowel >= 3 or constant >= 3:
                accep = 0

            prev = i

    if accep == 1 and is_vowel:
        print(f"<{temp}> is acceptable.")
    else:
        print(f"<{temp}> is not acceptable.")
