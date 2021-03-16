from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    pool = [input() for _ in range(N)]
    visited = [[1000000000]*M for _ in range(N)]
    Q = deque()

    for i in range(N):
        for j in range(M):
            if pool[i][j] == 'W':
                Q.append((i, j))
                visited[i][j] = 0

    while Q:
        wx, wy = Q.popleft()
        for mode in range(4):
            nx = wx + dx[mode]
            ny = wy + dy[mode]
            if 0 <= nx < N and 0 <= ny < M and pool[nx][ny] == 'L' and visited[nx][ny] > visited[wx][wy] + 1:
                Q.append((nx, ny))
                visited[nx][ny] = visited[wx][wy] + 1

    ans = 0

    for line in range(N):
        ans += sum(visited[line])

    print(f'#{tc} {ans}')