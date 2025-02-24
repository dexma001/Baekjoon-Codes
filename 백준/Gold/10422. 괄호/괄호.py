import math

for _ in range(int(input())):
    n = int(input())
    print(0) if n%2 != 0 else print((math.factorial(2*(n//2))//(math.factorial(n//2)*math.factorial((n//2)+1)))%1000000007)