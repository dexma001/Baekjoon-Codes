answer = 0
for _ in range(int(input())):
    temp = str(input())
    if '01' in temp or 'OI' in temp:
        answer += 1
print(answer)