n = int(input())
temp = str(bin(n)[2:])

answer = 0
for i in range(len(temp)):
    if temp[i] != '0':
        answer += 3**(len(temp)-i-1)

print(answer)
