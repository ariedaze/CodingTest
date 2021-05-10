from collections import deque


dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

for tc in range(int(input())):
    I = int(input())
    starti, startj = map(int, input().split())
    targeti, targetj = map(int, input().split())
    visited = [[0]*I for _ in range(I)]

    Q = deque([(starti, startj, 0)])
    visited[starti][startj] = 1

    while Q:
        i, j, cnt = Q.popleft()

        if i == targeti and j == targetj:
            print(cnt)
            break

        for mode in range(8):
            nx = i + dx[mode]
            ny = j + dy[mode]

            if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]:
                visited[nx][ny] = 1
                Q.append((nx, ny, cnt+1))
