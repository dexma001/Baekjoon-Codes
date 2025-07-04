n, a, b, c = map(int, input().split())

import math

print(int(math.factorial(n) / (math.factorial(a) * math.factorial(b) * math.factorial(c))))