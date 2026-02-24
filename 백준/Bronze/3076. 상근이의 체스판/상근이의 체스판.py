r, c = map(int, input().split())
a, b = map(int, input().split())

answer = list()

for k in range(r):
    for i in range(a):
        answer.append(list())
        for j in range(c):
            if k % 2 == 0:
                if j % 2 == 0:
                    for _ in range(b):
                        answer[-1].append("X")
                else:
                    for _ in range(b):
                        answer[-1].append(".")
            else:
                if j % 2 == 0:
                    for _ in range(b):
                        answer[-1].append(".")
                else:
                    for _ in range(b):
                        answer[-1].append("X")
                        
for i in answer:
    print(''.join(i))