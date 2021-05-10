import sys; sys.stdin = open('input_data/2206.txt')
from collections import deque
from pprint import pprint

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

height, width = map(int, sys.stdin.readline().split())
Ground = [list(map(int, ' '.join(sys.stdin.readline()).split())) for _ in range(height)]
visit = [[10000]*width for _ in range(height)]
Q = deque()
Q.append([0, 0, False, 1])
visit[0][0] = 1
while Q:
    x, y, attack, depth = Q.popleft()
    if depth > visit[height-1][width-1]:
        break
    if [x, y] == [height-1, width-1]:
        result = depth
    visit[x][y] = depth
    depth += 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width:
            visit[tx][ty] = depth
            if not Ground[tx][ty]:
                Q.append([tx, ty, attack, depth])
            elif not attack:
                Q.append([tx, ty, not attack, depth])
pprint(visit)
if visit[height-1][width-1] == 10000:
    print(-1)
else:
    print(visit[height-1][width-1])