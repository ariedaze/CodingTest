#TODO 높이 잘 조져보면 될듯?!!?

import sys; sys.stdin = open('input_data/3055.txt')
from pprint import pprint
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

height, width = map(int, sys.stdin.readline().split())
Ground = [list(' '.join(sys.stdin.readline()).split()) for _ in range(height)]
water_list = deque()
result = "KAKTUS"
visit = [[100]*width for _ in range(height)]
Q = deque()
for i in range(height):
    for j in range(width):
        if Ground[i][j] == "*":
            Ground[i][j] = 1
            water_list.append([i, j, 1])
        elif Ground[i][j] == "S":
            Q.append([i, j, 1])
        elif Ground[i][j] == "D":
            hole = [i, j]

while water_list:
    x, y, depth = water_list.popleft()
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width and (Ground[tx][ty] == "." or Ground[tx][ty] == "S"):
            Ground[tx][ty] = depth + 1
            water_list.append([tx, ty, depth + 1])
while Q:
    x, y, depth = Q.popleft()
    visit[x][y] = depth
    depth += 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if [tx, ty] == hole:
            if type(result) == int and depth -1 < result:
                result = depth - 1
            else:
                result = depth - 1
        if 0 <= tx < height and 0 <= ty < width and type(Ground[tx][ty]) == int and visit[tx][ty] > depth and Ground[tx][ty] > depth:
            visit[tx][ty] = depth
            Q.append([tx, ty, depth])
        elif 0 <= tx < height and 0 <= ty < width and Ground[tx][ty] == "." and visit[tx][ty] > depth:
            visit[tx][ty] = depth
            Q.append([tx, ty, depth])

print(result)