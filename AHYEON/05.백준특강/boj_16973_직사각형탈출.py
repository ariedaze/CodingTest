from collections import deque

def check(x, y):
    for i in range(x, x+H):
        for j in range(y, y+W):
            if not (0 <= i < N) or not (0 <= j < M) or arr[i][j] == 1:
                return False
    return True


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[987654321]*M for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

Q = deque([(Sr-1, Sc-1)])
visited[Sr-1][Sc-1] = 0

while Q:
    x, y = Q.popleft()
    for mode in range(4):
        nx, ny = x + dx[mode], y + dy[mode]
        if check(nx, ny) and visited[nx][ny] > visited[x][y] + 1:
            Q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

if visited[Fr-1][Fc-1] == 987654321:
    print(-1)
else:
    print(visited[Fr-1][Fc-1])