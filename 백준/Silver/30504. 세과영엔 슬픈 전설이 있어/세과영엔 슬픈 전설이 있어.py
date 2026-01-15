import sys
input = sys.stdin.readline

n = int(input())

temp_A = list(map(int, input().split()))
temp_B = list(map(int, input().split()))
temp_B.sort()

A = list()
for i in range(n):
    A.append([i, temp_A[i]])
    
A.sort(key=lambda x:[x[1]])
B = list()

for i in range(n):
    if A[i][1] > temp_B[i]:
        print(-1)
        quit()

    else:
        B.append([temp_B[i], A[i][0]])
        
B.sort(key=lambda x:[x[1]])

answer = list()

for i in B:
    answer.append(i[0])
    
print(*answer)
