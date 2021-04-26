import sys
from collections import deque

knight_dx = [-2, -2, 2, 2, -1, -1, 1, 1]
knight_dy = [1, -1, 1, -1, 2, -2, 2, -2]

bishop_dx = [1, 1, -1, -1]
bishop_dy = [1, -1, 1, -1]

rook_dx = [1, -1, 0, 0]
rook_dy = [0, 0, 1, -1]

rook = 0
bishop = 1
knight = 2

ln = sys.stdin.readline
q = deque()

N = int(ln())
arr = []
visit = [[[[[False] for _ in range(3)] for _ in range(N ** 2)] for _ in range(N)] for _ in range(N)]
# print(visit)

for i in range(N):
    arr.append(list(map(int, ln().split())))
    for j in range(N):
        if arr[i][j] == 1:
            x, y = i, j
            break


def bfs(x, y):
    q.append([x, y, 0, 2, rook])
    q.append([x, y, 0, 2, bishop])
    q.append([x, y, 0, 2, knight])

    visit[x][y][2][rook] = True
    visit[x][y][2][bishop] = True
    visit[x][y][2][knight] = True

    while q:
        x, y, cnt, next, flag = q.popleft()
        if next == N ** 2:
            return cnt


        for i in range(3):
            if i == flag:
                continue
            if visit[x][y][next][i]:
                continue
            visit[x][y][next][i] = True
            q.append([x, y, cnt + 1, next, i])

        if flag == rook:
            for i in range(4):
                tx, ty = x + rook_dx[i], y + rook_dy[i]
                if 0 <= tx < N and 0 <= ty < N and not visit[tx][ty][next][rook]:
                    visit[tx][ty][next][rook] = True
                # if tx ==

        elif flag == bishop:
            pass

        elif flag == knight:
            pass




print(bfs(x, y))
