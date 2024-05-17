# 1309

n = int(input())
x, y, z = 1, 1, 1

for _ in range(n-1):
    x1 = x+y+z
    y1 = x+z
    z1 = x+y
    x, y, z = x1, y1, z1

print((x + y + z) % 9901)
