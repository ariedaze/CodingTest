import sys
from collections import deque

ln = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

lst = [list(ln().rstrip()) for _ in range(12)]


def bfs(x, y):
    stack = []
    q = deque()
    visit[x][y] = 1
    q.append([x, y])
    stack.append([x, y])
    while q:
        x, y = q.popleft()
        for d in range(4):
            tx, ty = x + dx[d], y + dy[d]
            if 0 <= tx < 12 and 0 <= ty < 6 and lst[x][y] == lst[tx][ty] and not visit[tx][ty]:
                q.append([tx, ty])
                visit[tx][ty] = 1
                stack.append([tx, ty])
    return stack


def gravity(lst):
    for j in range(6):
        g_cnt = []
        for i in range(11, -1, -1):
            if lst[i][j] != '.':
                g_cnt.append(lst[i][j])
                lst[i][j] = '.'

        for g in range(len(g_cnt)):
            lst[11 - g][j] = g_cnt[g]
    return lst


ans = 0
while True:
    visit = [[0] * 6 for _ in range(12)]
    s = []
    for i in range(12):
        for j in range(6):
            if visit[i][j] == 0 and lst[i][j] != '.':
                stack = bfs(i, j)
                if len(stack) >= 4:
                    s += stack
    if len(s) > 0:
        ans += 1
        for k in range(len(s)):
            x, y = s[k][0], s[k][1]
            lst[x][y] = '.'
    else:
        break
    gravity(lst)


print(ans)