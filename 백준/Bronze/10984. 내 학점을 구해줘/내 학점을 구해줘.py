for _ in range(int(input())):
    n = int(input())
    grade = 0
    average = 0

    for _ in range(n):
        a, b = map(float, input().split())
        a = int(a)
        grade += a
        average += a*b

    print(grade,  round(average/grade, 1))
