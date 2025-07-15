s = str(input())
t = str(input())

ns = s * len(t)
nt = t * len(s)

print(1 if ns == nt else 0)