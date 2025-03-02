temp = list()

for i in range(1, 9):
    t = int(input())
    temp.append([t, i])
    
temp.sort(reverse = True)

answer = 0
answer_li = list()

for i, j in temp[:5]:
    answer += i
    answer_li.append(j)
    
answer_li.sort()

print(answer)
print(*answer_li)