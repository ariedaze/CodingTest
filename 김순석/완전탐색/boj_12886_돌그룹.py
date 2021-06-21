import sys
from collections import deque
ln = sys.stdin.readline

A, B, C = map(int, ln().split())
visit = [[0] * 1501 for _ in range(1501)]
val = A + B + C

def bfs():
    q = deque()
    q.append((A, B))
    visit[A][B] = 1

    while q:
        x, y = q.popleft()
        z = val - x - y
        if x == y == z:
            return 1
        for tx, ty in ((x, y), (y, z), (z, x)):
            if tx < ty:
                ty -= tx
                tx += tx
            elif tx > ty:
                tx -= ty
                ty += ty

            tz = val - tx - ty
            x = min((min(tx, ty), tz))
            y = max((max(tx, ty), tz))

            if not visit[x][y]:
                q.append((x, y))
                visit[x][y] = 1
    return 0


if (A + B + C) % 3 != 0:
    print(0)
    exit()

else:
    print(bfs())

