# 2504

arr = list(map(str, input().strip()))

answer = 0
ratio = 1
stack = list()

for i in range(len(arr)):
    if arr[i] == '(':
        ratio *= 2
        stack.append(arr[i])
    elif arr[i] == '[':
        ratio *= 3
        stack.append(arr[i])
    elif arr[i] == ')':
        if not stack:
            print(0)
            quit()
        elif stack and stack[-1] == '[':
            print(0)
            quit()
        else:
            stack.pop()
            if arr[i-1] == ']' or arr[i-1] == ')':
                ratio //= 2
            else:
                answer += ratio
                ratio //= 2
    else:
        if not stack:
            print(0)
            quit()

        elif stack and stack[-1] == '(':
            print(0)
            quit()
        else:
            stack.pop()
            if arr[i-1] == ']' or arr[i-1] == ')':
                ratio //= 3
            else:
                answer += ratio
                ratio //= 3

print(0) if stack else print(answer)
