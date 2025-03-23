a,b,c = map(int, input().split())
one = 0
two = 0

for i in [a, b, c]:
    if i == 1:
        one += 1
    else:
        two += 1
        
print(2) if two > one else print(1)