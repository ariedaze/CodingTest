import sys
from collections import deque
ln = sys.stdin.readline

# 서 북 동 남
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

m, n = map(int, ln().split())
arr = [list(map(int, ln().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]


def bfs(x, y, direction):
    global room
    q = deque()
    q.append([x, y, direction])
    visit[x][y] = area
    while q:
        x, y, direction = q.popleft()
        wall = check(direction)

        for i in range(4):
            if wall[i] == 0:
                tx, ty = x + dx[i], y + dy[i]
                if 0 <= tx < n and 0 <= ty < m and visit[tx][ty] == 0:
                    visit[tx][ty] = area
                    q.append([tx, ty, arr[tx][ty]])
                    room += 1

    return


def check(x):
    # w, n, e, s
    d = []
    while len(d) <= 3:
        d.append(x % 2)
        x //= 2
    return d


room = 1
area = 1
max_len = 0
max_size = 0
tmp = [0]
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            bfs(i, j, arr[i][j])
            if room > max_len:
                max_len = room
            tmp.append(room)
            room = 1
            area += 1

print(area - 1)
print(max_len)
# print(tmp)

for x in range(n):
    for y in range(m):
        for d in range(4):
            tx, ty = x + dx[d], y + dy[d]
            if 0 <= tx < n and 0 <= ty < m and visit[x][y] != visit[tx][ty]:
                val = tmp[visit[x][y]] + tmp[visit[tx][ty]]
                if max_size < val:
                    max_size = val
print(max_size)