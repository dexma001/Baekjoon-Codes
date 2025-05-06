a,b,c =map(int, input().split())
x,y,z = map(int, input().split())

print('YES') if (x-a)**2 + (y-b)**2 < (c+z)**2 else print('NO')