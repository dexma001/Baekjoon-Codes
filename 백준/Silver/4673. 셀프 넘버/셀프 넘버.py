import sys
input = sys.stdin.readline

nums = [i + 1 for i in range(10000)] # 1 to 10000
dns = []

for num in nums:
    ans = num
    temp = len(str(num)) #정수의 길이
    for i in range(temp):
        ans += num//(10**(temp-(i+1)))
        num %= 10**(temp-(i+1))
    
    dns.append(ans)

dns = (set(dns)) # save unique values

for dn in dns:
    if dn > 10000:
        continue

    nums.remove(dn)

# print every line
for num in nums:
    print(num)
    
