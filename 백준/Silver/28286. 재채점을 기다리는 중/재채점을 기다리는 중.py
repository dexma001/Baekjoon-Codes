n, k = map(int, input().split())
ans = list(map(int, input().split()))
omr = list(map(int, input().split()))

answer = 0

def brute_force(ans, omr, cnt):
    global answer
    temp_answer = 0
    for i in range(n):
        if ans[i] == omr[i]:
                temp_answer += 1
    answer = max(answer, temp_answer)
    if cnt == k:
        return
    
    else:
        for i in range(n):
            if i == 0:
                t_omr = [-1] + omr[i:-1]
                brute_force(ans, t_omr, cnt+1)
            elif i == n-1:
                t_omr = omr[1:] + [-1]
                brute_force(ans, t_omr, cnt+1)
            else:
                t_omr = omr[:i] + [-1] + omr[i:-1]
                brute_force(ans, t_omr, cnt+1)
                t_omr = omr[:i] + omr[i+1:] + [-1]
                brute_force(ans, t_omr, cnt+1)

brute_force(ans, omr, 0)
print(answer)