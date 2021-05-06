#TODO 높이 잘 조져보면 될듯?!!?

import sys; sys.stdin = open('input_data/3055.txt')
from copy import deepcopy
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

height, width = map(int, sys.stdin.readline().split())
Ground = []
hole = list()
quokka = list()
water_list = deque()
for i in range(height):
    line = list(' '.join(sys.stdin.readline()).split())
    Ground.append(line)
    if not hole:
        if "D" in line:
            hole = [i, line.index("D")]
    if not quokka:
        if "S" in line:
            quokka = [i, line.index("S")]
    if line.count("*") > 1:
        for j in range(len(line)):
            if line[j] == "*":
                water_list.append([i,j])
    elif line.count("*") == 1:
        water_list.append([i,line.index("*")])

visit = [[0]*width for _ in range(height)]
origin = width * (height//2 + 1)
Max = origin
Q = deque()
Q.append([quokka[0], quokka[1], 0, Ground, visit, water_list])

while Q:
    x, y, depth, my_ground, my_visit, my_water_list = Q.popleft()
    now_ground = deepcopy(my_ground)
    now_visit = deepcopy(my_visit)
    now_water = []
    now_visit[x][y] = 1
    while my_water_list:
        water_x, water_y = my_water_list.pop()
        for k in range(4):
            tx = water_x + dx[k]
            ty = water_y + dy[k]
            if 0 <= tx < height and 0 <= ty < width and [tx, ty] not in now_water and (
                    my_ground[tx][ty] == "." or my_ground[tx][ty] == "S"):
                now_ground[tx][ty] = "*"
                now_water.append([tx, ty])

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width and now_ground[tx][ty] == "D":
            if Max > depth + 1:
                Max = depth + 1
                pass
        if 0 <= tx < height and 0 <= ty < width and now_ground[tx][ty] == "." and not now_visit[tx][ty]:
            go_water = deepcopy(now_water)
            Q.append([tx, ty, depth + 1, now_ground, now_visit, go_water])

if Max == origin:
    print("KAKTUS")
else:
    print(Max)