from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    q = deque()
    q.append([0,0])
    while q:
        x, y = q.popleft()

        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or tx == n or ty < 0 or ty == m:
                continue
            if not visited[tx][ty] and maps[tx][ty]:
                visited[tx][ty] = visited[x][y] + 1
                q.append([tx,ty])

    if visited[n - 1][m - 1]:
        answer = visited[n - 1][m - 1]
    else:
        answer = -1

    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))