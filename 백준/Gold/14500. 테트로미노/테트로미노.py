import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0

for i in range(n):
    for j in range(m):
        case = []
        for p in range(4):
            x = j + dx[p]
            y = i + dy[p]
            if -1 < x < m and -1 < y < n:
                case.append([[i, j], [y, x]])
            for k in range(len(case)):  # 총 길이
                value = 0
                case_border = []
                for q in range(len(case[k])):  # 2
                    for l in range(4):
                        x1 = case[k][q][1] + dx[l]
                        y1 = case[k][q][0] + dy[l]
                        if -1 < x1 < m and -1 < y1 < n and [y1, x1] not in case[k]:
                            case_border.append(li[y1][x1])
                    value += li[case[k][q][0]][case[k][q][1]]
                case_border.sort(reverse=True)
                value += case_border[0] + case_border[1]
                if value > ans:
                    ans = value

print(ans)
