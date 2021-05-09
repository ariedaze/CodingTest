import sys
from collections import deque

ln = sys.stdin.readline
q = deque()
q_water = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# R, C, 행, 렬
# *, X 물, 돌
# D, S 비버굴, 고슴도치
R, C = map(int, ln().split())
lst = []

visit = [[0] * C for _ in range(R)]


def bfs(x, y):
    q.append([x, y])
    visit[x][y] = 1

    while q:
        cnt = len(q)
        while cnt:
            x, y = q.popleft()

            for i in range(4):
                tx, ty = x + dx[i], y + dy[i]

                if tx < 0 or tx >= R or ty < 0 or ty >= C:
                    continue
                if tx == ex and ty == ey:
                    return visit[x][y]
                if visit[tx][ty] == 0 and lst[tx][ty] == '.':
                    visit[tx][ty] = visit[x][y] + 1
                    q.append([tx, ty])
            cnt -= 1
        water()
    return 'KAKTUS'


def water():
    q_len = len(q_water)
    while q_len:
        x, y = q_water.popleft()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]

            if tx < 0 or tx >= R or ty < 0 or ty >= C:
                continue
            if lst[tx][ty] == '.':
                lst[tx][ty] = '*'
                q_water.append([tx, ty])
        q_len -= 1


for i in range(R):
    lst.append(list(ln().rstrip()))
    for j in range(C):
        if lst[i][j] == '*':
            q_water.append([i, j])
        if lst[i][j] == 'D':
            ex, ey = i, j
        if lst[i][j] == 'S':
            x, y = i, j
            lst[i][j] = '.'

water()
print(bfs(x, y))
