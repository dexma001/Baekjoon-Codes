n, w, h = map(int, input().split())
side = (w**2 + h**2)**(0.5)

for _ in range(n):
    if int(input()) <= side:
        print("DA")
    else:
        print("NE")