n,l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse = True)

while arr and arr[-1] <= l:
    l += 1
    arr.pop()
    
print(l)