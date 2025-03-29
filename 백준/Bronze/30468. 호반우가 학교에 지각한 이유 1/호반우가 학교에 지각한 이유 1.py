#30468

a,b,c,d,e = map(int, input().split())
print(max(e*4-(a+b+c+d), 0))