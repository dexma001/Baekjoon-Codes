n = int(input())
temp = list(set(map(int, input().split())))
temp.sort()
print(*temp)