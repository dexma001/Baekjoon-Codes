n, answer, k = map(int, input().split())

for _ in range(k):
    a, b = map(int, input().split())
    if a == answer:
        answer = b
    elif b == answer:
        answer = a
    else:
        continue
    
print(answer)