from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
visit = [[0] * N for _ in range(N)]

q = deque()
q.append((r1, c1, 0))
visit[r1][c1] = 1
ans = -1
while q:
    x, y, mov = q.popleft()
    for i in range(6):
        tx, ty = x + dx[i], y + dy[i]
        if tx == r2 and ty == c2:
            ans = mov + 1
            print(ans)
            exit()
        if 0 <= tx < N and 0 <= ty < N and visit[tx][ty] == 0:
            visit[tx][ty] = 1
            q.append((tx, ty, mov + 1))

print(ans)