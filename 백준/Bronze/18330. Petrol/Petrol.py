n = int(input())
m = int(input())
m += 60

print(min(m, n)*1500 + max(0, n-m) * 3000)