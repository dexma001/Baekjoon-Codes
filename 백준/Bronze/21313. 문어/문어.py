n = int(input())
arr = [1, 2] * (n//2) + ([3] if n % 2 else [])
print(*arr)