from collections import deque

dx = [1, -1, 0, 0]
dy = [0 ,0, 1, -1]

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
height = len(maps)
width = len(maps[0])
visit = [[10000]*width for _ in range(height)]
visit[0][0] = 1

Q = deque()
Q.append([0, 0])
while Q:
    x, y = Q.popleft()
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width and maps[tx][ty] and visit[tx][ty] > visit[x][y] + 1:
            visit[tx][ty] = visit[x][y] + 1
            Q.append([tx, ty])
    result = visit[height - 1][width - 1]
    if result == 10000:
        print(-1)
    else:
        print(result)



