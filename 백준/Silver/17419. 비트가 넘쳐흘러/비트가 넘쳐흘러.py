a = int(input())
n = str(input())
n = int(n, 2)

answer = 0
while n != 0:
    n = n-(n & ((~n)+1))
    answer += 1

print(answer)
