import sys; sys.stdin = open('input_data/2178.txt')
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
height, width = map(int, input().split())
ground = [list(map(int, ' '.join(input()).split())) for _ in range(height)]
visit = [[0]*width for _ in range(height)]

Q = deque()
Q.append([0, 0])
visit[0][0] = 1
while Q:
    x, y = Q.popleft()
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width and not visit[tx][ty] and ground[tx][ty]:
            visit[tx][ty] = visit[x][y] + 1
            Q.append([tx, ty])
print(visit[height- 1][width - 1])

