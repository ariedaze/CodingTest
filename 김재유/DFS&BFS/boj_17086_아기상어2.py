import sys; sys.stdin = open('input_data/17086.txt')
from collections import deque

dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [1, -1, 1, -1, 0, 0, 1, -1]

height, width = map(int, input().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
check = [[100000]*width for _ in range(height)]

Q = deque()
for x in range(height):
    for y in range(width):
        if ground[x][y]:
            Q.append([x, y, 1])
            check[x][y] = 1
while Q:
    x, y, depth = Q.popleft()
    if check[x][y] < depth:
        check[x][y] = depth
    for i in range(8):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width and depth + 1 < check[tx][ty]:
            Q.append([tx, ty, depth + 1])
            check[tx][ty] = depth + 1
result = 0
for line in check:
    if max(line) > result:
        result = max(line)
print(result-1)


