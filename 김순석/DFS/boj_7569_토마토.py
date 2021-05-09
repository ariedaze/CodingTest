# pypy로 제출
from collections import deque

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
M, N, H = map(int, input().split())

G = []
q = deque()
for _ in range(H):
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    G.append(arr)

for h in range(H):
    for i in range(N):
        for j in range(M):
            if G[h][i][j] == 1:
                q.append([h, i, j])

while q:
    z, x, y = q.popleft()
    for i in range(6):
        tz, tx, ty = z + dz[i], x + dx[i], y + dy[i]

        if tz <= -1 or tz >= H or tx <= -1 or tx >= N or ty <= -1 or ty >= M:  continue
        if G[tz][tx][ty] == -1: continue
        if G[tz][tx][ty] == 0:
            G[tz][tx][ty] = G[z][x][y] + 1
            q.append([tz, tx, ty])

max_val = 0
status = True
for k in range(H):
    for i in range(N):
        for j in range(M):
            if G[k][i][j] == 0:
                status = False
                break
            if G[k][i][j] > max_val:
                max_val = G[k][i][j]
if status:
    print(max_val - 1)
else:
    print(-1)
