n = int(input())

for _ in range(n):
    index = str(input())
    total = 0
    student = int(input())
    for _ in range(student):
        total += int(input())

    print('YES') if total % student == 0 else print('NO')
