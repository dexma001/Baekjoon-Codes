n = int(input())
s1 = list(map(int, input().split()))
s1 = set(s1)

m = int(input())
s2 = list(map(int, input().split()))

answer = []
for i in range(m):
    if s2[i] in s1:
        answer.append('1')
    else:
        answer.append('0')

print(' '.join(answer))
