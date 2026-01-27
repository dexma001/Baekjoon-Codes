n = int(input())

top = list(map(int, input().split()))
bottom = list(map(int, input().split()))

answer = list()
answer.append(0)

for i in range(1, n-1):
    high = min(top[i], top[i-1], top[i+1]) - 1 
    low = max(bottom[i], bottom[i-1], bottom[i+1]) + 1

    if bottom[i] < answer[-1] and answer[-1] < top[i]:
        answer.append(answer[-1])
    else:
        if abs(high - answer[-1]) < abs(answer[-1] - low):
            answer.append(high)
        elif abs(high - answer[-1]) == abs(answer[-1] - low):
            answer.append(high if abs(high) < abs(low) else low)
        else:
            answer.append(low)

answer.append(0)

print(*answer)