a, b = map(int, input().split())
temp = int(str(a)[::-1]) + int(str(b)[::-1])
print(int(str(temp)[::-1]))
