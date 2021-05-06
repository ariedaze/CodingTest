import sys; sys.stdin = open('input_data/3055.txt')
from copy import deepcopy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x, y, depth, Ground, visit, water_list):
    global Max
    now_ground = deepcopy(Ground)
    now_visit = deepcopy(visit)
    now_water = []
    if depth >= Max:
        return
    now_visit[x][y] = 1
    while water_list:
        water_x, water_y = water_list.pop()
        for k in range(4):
            tx = water_x + dx[k]
            ty = water_y + dy[k]
            if 0 <= tx < height and 0 <= ty < width and [tx, ty] not in water_list and (Ground[tx][ty] == "." or Ground[tx][ty] == "S"):
                now_ground[tx][ty] = "*"
                now_water.append([tx, ty])

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width and now_ground[tx][ty] == "D":
            if Max > depth + 1:
                Max = depth + 1
                return
        if 0 <= tx < height and 0 <= ty < width and now_ground[tx][ty] == "." and not visit[tx][ty]:
            DFS(tx, ty, depth+1, now_ground, now_visit, now_water)

height, width = map(int, sys.stdin.readline().split())
Ground = []
hole = list()
quokka = list()
water_list = []
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
        for j in range(line):
            water_list.append([i,j])
    elif line.count("*") == 1:
        water_list.append([i,line.index("*")])
visit = [[0]*width for _ in range(height)]
origin = width * (height//2 + 1)
Max = origin
DFS(quokka[0], quokka[1], 0, Ground, visit, water_list)
if Max == origin:
    print("KAKTUS")
else:
    print(Max)