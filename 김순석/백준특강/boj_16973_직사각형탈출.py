# 시간초과나서 pypy로 제출
import sys
from collections import deque

ln = sys.stdin.readline

# 오 왼 아래 위
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


N, M = map(int, ln().split())
arr = [list(map(int, ln().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, ln().split())
visit = [[0] * M for _ in range(N)]


def bfs(x, y, cnt):
    q = deque()
    q.append((x, y, cnt))
    while q:
        x, y, cnt = q.popleft()
        if x == Fr - 1 and y == Fc - 1:
            return cnt

        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < N and 0 <= ty < M and 0 <= tx + H - 1 < N and 0 <= ty + W - 1 < M and not visit[tx][ty]:
                if check(i, tx, ty):
                    visit[tx][ty] = True
                    q.append((tx, ty, cnt + 1))

    return -1


# 오 왼 아래 위
def check(dir, tx, ty):
    if dir == 0:
        for i in range(H):
            if arr[tx + i][ty + W - 1] == 1:
                return False
    elif dir == 1:
        for i in range(H):
            if arr[tx + i][ty] == 1:
                return False

    elif dir == 2:
        for i in range(W):
            if arr[tx + H - 1][ty + i] == 1:
                return False

    elif dir == 3:
        for i in range(W):
            if arr[tx][ty + i] == 1:
                return False
    return True


print(bfs(Sr - 1, Sc - 1, 0))