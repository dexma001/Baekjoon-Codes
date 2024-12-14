import sys
input = sys.stdin.readline

n = int(input())
p = int(input())

answer = 50000

if n >= 20:
    answer = min(p//4*3, p-2000)

elif n >= 15:
    answer = min(p//10*9, p-2000)

elif n >= 10:
    answer = min(p//10*9, p-500)

elif n >= 5:
    answer = p-500

else:
    answer = p

if answer < 0:
    answer = 0
print(answer)
