a, b = map(int, input().split())
c, d=  map(int, input().split())

x = a + c
y = b + d

if x < y:
    print("Hanyang Univ.")
elif x > y:
    print("Yongdap")
else:
    print("Either")