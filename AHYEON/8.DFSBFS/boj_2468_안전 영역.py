import sys
sys.setrecursionlimit(100000)


def dfs(x, y, k):
    for mode in range(4):
        nx = x + dx[mode]
        ny = y + dy[mode]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] > k:
            visited[nx][ny] = 1
            dfs(nx, ny, k)


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 1

for k in range(max(map(max, graph))):
    visited = [[0]*N for _ in range(N)]
    candi = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and not visited[i][j]:
                candi += 1
                visited[i][j] = 1
                dfs(i, j, k)
    ans = max(ans, candi)

print(ans)
