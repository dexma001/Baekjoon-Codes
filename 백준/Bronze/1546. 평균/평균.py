n = int(input())
li = list(map(int, input().split()))

k = max(li)

for i in range(n):
    li[i] = (li[i]/k) * 100

print(sum(li)/n)
