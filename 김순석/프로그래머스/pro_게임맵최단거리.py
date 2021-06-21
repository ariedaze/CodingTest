dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
from collections import deque

def solution(maps):
    answer = -1
    n = 0
    for i in maps:
        m = len(i)
        n += 1
    answer = bfs(0, 0, n, m, maps)
    return answer


def bfs(x, y, n, m, maps):
    visit = [[-1] * m for _ in range(n)]
    visit[x][y] = 1
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]

            if 0 <= tx < n and 0 <= ty < m and visit[tx][ty] == -1 and maps[tx][ty]:
                visit[tx][ty] = visit[x][y] + 1
                q.append([tx, ty])
    return visit[n - 1][m - 1]

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))