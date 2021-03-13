from collections import deque

N, M, K = map(int, input().split())
graph = [[0]*(M+1) for _ in range(N+1)]
visited = [[0]*(M+1) for _ in range(N+1)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(K):
    r, c = map(int, input().split())
    graph[r][c] = 1

cnt = ans = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] and not visited[i][j]:
            cnt = 1
            Q = deque([(i, j)])
            visited[i][j] = 1
            while Q:
                x, y = Q.popleft()
                for mode in range(4):
                    nx = x + dx[mode]
                    ny = y + dy[mode]
                    if 0 < nx <= N and 0 < ny <= M and graph[nx][ny] and not visited[nx][ny]:
                        Q.append((nx, ny))
                        visited[nx][ny] = 1
                        cnt += 1
        ans = max(ans, cnt)

print(ans)