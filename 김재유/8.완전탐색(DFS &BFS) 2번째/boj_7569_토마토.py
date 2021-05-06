import sys; sys.stdin = open('input_data/7569.txt')

from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

width, height, stack = map(int,input().split())
ground = []
visit = []
for _ in range(stack):
    ground.append([list(map(int, sys.stdin.readline().split())) for _ in range(height)])
    visit.append([[0] * width for _ in range(height)])
Q = deque()
go_check = width * height * stack
for z in range(stack):
    for y in range(width):
        for x in range(height):
            if ground[z][x][y] == 1:
                Q.append([x, y, z])
                visit[z][x][y] = 1
                go_check -= 1
            elif ground[z][x][y] == -1:
                visit[z][x][y] = -1
                go_check -= 1
max_count = 0
while Q:
    x, y, z = Q.popleft()
    if visit[z][x][y] > max_count:
        max_count = visit[z][x][y]
    for i in range(6):
        tx = x + dx[i]
        ty = y + dy[i]
        tz = z + dz[i]
        if 0 <= tx < height and 0 <= ty < width  and 0 <= tz < stack and not visit[tz][tx][ty] and not visit[tz][tx][ty] == -1:
            visit[tz][tx][ty] = visit[z][x][y] + 1
            go_check -= 1
            Q.append([tx, ty, tz])
if go_check:
    print(-1)
else:
    print(max_count-1)