import sys
input = sys.stdin.readline

number = {'1': "one", "2" : "two", "3" : "three", "4" : "four", "5" : "five", "6" : "six", "7" : "seven", "8" : "eight", "9" : "nine", "0" : "zero"}

m, n = map(int, input().split())

arr = list()

for i in range(m, n+1):
    temp = ''
    for j in str(i):
        temp += number[j]
    
    arr.append([temp, i])
    
arr.sort(key=lambda x:[x[0]])

temp = list()
for i in arr:
    temp.append(i[1])
    if len(temp) == 10:
        print(*temp)
        temp = list()
        
print(*temp)