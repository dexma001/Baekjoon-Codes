answer = 0

t, start = map(int, input().split())
answer = start + 1 - 1

for _ in range(3):
    minus, plus = map(int, input().split())
    start = start - minus + plus
    answer = max(start, answer)

print(answer)
