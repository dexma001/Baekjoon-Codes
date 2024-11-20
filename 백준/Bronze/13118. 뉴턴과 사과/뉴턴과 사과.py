arr = list(map(int, input().split()))
x, y, r = map(int, input().split())
print(arr.index(x)+1) if x in arr else print(0)
