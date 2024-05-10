# 20149

import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

point = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]


def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])


def check():
    if ccw(point[0], point[1], point[2]) * ccw(point[0], point[1], point[3]) == 0 and ccw(point[2], point[3], point[0]) * ccw(point[2], point[3], point[1]) == 0:
        if point[0] > point[1]:
            point[0], point[1] = point[1], point[0]
        if point[2] > point[3]:
            point[2], point[3] = point[3], point[2]
        if point[1] >= point[2] and point[0] <= point[3]:
            return True
        else:
            return False

    if ccw(point[0], point[1], point[2]) * ccw(point[0], point[1], point[3]) <= 0 and ccw(point[2], point[3], point[0]) * ccw(point[2], point[3], point[1]) <= 0:
        return True

    return False


if check():
    print(1)
    try:
        x = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)) / \
            ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        y = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)) / \
            ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        print(x, y)
    except:
        if point[0] > point[1]:
            point[0], point[1] = point[1], point[0]
        if point[2] > point[3]:
            point[2], point[3] = point[3], point[2]
        if point[0] == point[3]:
            print(point[0][0], point[0][1])
        elif point[1] == point[2]:
            print(point[1][0], point[1][1])


else:
    print(0)
