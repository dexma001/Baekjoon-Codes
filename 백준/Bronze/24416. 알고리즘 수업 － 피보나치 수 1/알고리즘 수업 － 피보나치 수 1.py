# 24416

n = int(input())
answer = 0


def fib(n):
    global answer
    if n == 1 or n == 2:
        answer += 1
        return 1
    else:
        return (fib(n-1) + fib(n-2))


fib(n)
print(answer, n-2)
