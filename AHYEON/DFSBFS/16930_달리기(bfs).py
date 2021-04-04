from collections import deque

N, M, K = map(int, input().split())
gym = [input() for _ in range(N)]
x1, y1, x2, y2 = map(int, input().split()); x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
visited = [[0]*M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

Q = deque([(x1, y1)])
ans = False

while Q:
    x, y = Q.popleft()
    if x == x2 and y == y2:
        ans = True
        break
    for mode in range(4):
        for num in range(1, K+1):
            nx = x + dx[mode]*num
            ny = y + dy[mode]*num
            if nx < 0 or nx >= N or ny < 0 or ny >= M or gym[nx][ny] == '#': break
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                Q.append((nx, ny))
            elif visited[nx][ny] == visited[x][y] + 1:
                continue  # 일단 직진
            else:
                break  # 더 큰길은 안감


if ans:
    print(visited[x2][y2])
else:
    print(-1)
