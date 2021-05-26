from collections import  deque


def bfs():
    q = deque()
    q.append([S[0], S[1], 0])

    while q:
        x, y, cnt = q.popleft()

        if x ==  D[0] and y == D[1]:
            return cnt
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if -1 < nx < R and -1 < ny < C and not visited[nx][ny]:
                visited[nx][ny] = True
                if arr[nx][ny] == '.' and cnt + 1 < flood_visited[nx][ny] or flood_visited[nx][ny] == -1:
                    q.append([nx, ny, cnt + 1])

    return 'KAKTUS'


def flood():
    global flood_queue
    tmp = deque()

    while flood_queue:
        for pos in flood_queue:
            x, y, cnt = pos
            for t in range(4):
                nx = x + dx[t]
                ny = y + dy[t]
                if -1 < nx < R and -1 < ny < C and arr[nx][ny] in '.' and flood_visited[nx][ny] == -1:
                    flood_visited[nx][ny] = cnt + 1
                    tmp.append([nx, ny, cnt + 1])
        flood_queue = tmp
        tmp = deque()



R, C = map(int, input().split())
arr = [input() for _ in range(R)]

flood_visited = [[-1] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]
# . empty  * water   X rock
# D 비버  S 고슴도치

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

flood_queue = deque()
S = [-1, -1]
D = [-1, -1]

for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            flood_visited[i][j] = 0
            flood_queue.append([i, j, 0])
        elif arr[i][j] == 'X':
            flood_visited[i][j] = 0
        elif arr[i][j] == 'S':
            visited[i][j] = True
            S = [i, j]
        elif arr[i][j] == 'D':
            D = [i, j]

flood()
answer = bfs()
print(answer)