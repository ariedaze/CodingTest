from collections import deque

pipe = {
    '1': [(-1, 0), (1, 0), (0, -1), (0, 1)],
    '2': [(1, 0), (-1, 0)],
    '3': [(0, -1), (0, 1)],
    '4': [(-1, 0), (0, 1)],
    '5': [(0, 1), (1, 0)],
    '6': [(1, 0), (0, -1)],
    '7': [(0, -1), (-1, 0)]
}

for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split()) # 세로, 가로, 멘홀, 시간
    tunnel = [input().split() for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    Q = deque([(R, C)])
    visited[R][C] = 1
    ans = 1
    while Q:
        x, y = Q.popleft()
        for dx, dy in pipe[tunnel[x][y]]: # 현재 칸 이동 가능 방향
            nx = x + dx
            ny = y + dy
            if visited[x][y] < L and 0 <= nx < N and 0 <= ny < M and tunnel[nx][ny] != '0' and not visited[nx][ny]:
                # 현재칸이랑 다음 칸이랑 연결 됨?
                if (-dx, -dy) in pipe[tunnel[nx][ny]]:
                    Q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    ans += 1

    print(f'#{tc} {ans}')