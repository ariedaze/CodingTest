from collections import  deque

N, M = map(int, input().split())
war = [input() for _ in range(M)]  # W: 우리팀  B: 적

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[0]*N for _ in range(M)]


def pow(x):
    return x**2


def bfs(i, j, cnt, team):
    Q = deque([(i, j)])
    visited[i][j] = 1
    while Q:
        x, y = Q.popleft()
        cnt += 1
        for mode in range(4):
            nx = x + dx[mode]; ny = y + dy[mode]
            if 0<=nx<M and 0<=ny<N and war[nx][ny] == team and not visited[nx][ny]:
                Q.append((nx, ny))
                visited[nx][ny] = 1
    return cnt


W_result = []
B_result = []

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            if war[i][j] == 'W':
                W_result.append(bfs(i, j, 0, 'W'))
            else:
                B_result.append(bfs(i, j, 0, 'B'))


print(sum(map(pow, W_result)), sum(map(pow, B_result)))
