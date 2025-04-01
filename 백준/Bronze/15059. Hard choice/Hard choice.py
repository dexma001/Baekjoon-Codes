a,b,c=map(int, input().split())
a1, b1, c1 = map(int, input().split())

print(abs(min(a-a1, 0) + min(b-b1, 0) +min(c-c1, 0)))