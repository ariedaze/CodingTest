from collections import deque
N, M = map(int, input().split())
graph = [input() for _ in range(N)]  # 1은 이

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[10000000]*M for _ in range(N)]

Q = deque([(0, 0)])
visited[0][0] = 1

while Q:
    vx, vy = Q.popleft()
    for mode in range(4):
        nx = vx + dx[mode]
        ny = vy + dy[mode]
        if 0<=nx<N and 0<=ny<M and graph[nx][ny]=='1':
            if visited[vx][vy] + 1 < visited[nx][ny]:
                visited[nx][ny] = visited[vx][vy] + 1
                Q.append((nx, ny))


print(visited[N-1][M-1])