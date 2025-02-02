from collections import defaultdict

temp = defaultdict(int)

for _ in range(9):
    temp[str(input())] += 1
    
print(max(temp.items(), key=lambda x:x[1])[0])