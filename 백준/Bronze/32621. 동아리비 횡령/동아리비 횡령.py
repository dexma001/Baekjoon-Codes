arr = str(input().strip())

for i in range(1, 1001):
    if str(i) + '+' + str(i) == arr:
        print("CUTE")
        break
    
else:
    print("No Money")