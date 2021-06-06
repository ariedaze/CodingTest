import sys
ln = sys.stdin.readline

N, M = map(int, ln().split())
ice = []
for _ in range(N):
    ice.append(list(map(int, ln().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit = [[0] * M for _ in range(N)]


def check(x, y):
    cnt = 0
    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]

        if 0 <= tx < N and 0 <= ty < M and ice[tx][ty] == 0:
            cnt += 1
    return cnt


def dfs(x, y):
    visit = [[0] * M for _ in range(N)]
    stack = [[x, y]]
    visit[x][y] = 1
    area = 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < N and 0 <= ty < M and ice[tx][ty] != 0 and visit[tx][ty] == 0:
                visit[tx][ty] = 1
                area += 1
                stack.append([tx, ty])
    return area


ans = 0
tmp = []
while True:
    tmp = []
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0:
                zero = check(i, j)
                tmp.append([i, j, zero])

    l_tmp = len(tmp)
    if len(tmp) == 0:
        print(0)
        break

    for i in range(len(tmp)):
        x, y = tmp[i][0], tmp[i][1]
        ice[x][y] -= tmp[i][2]
        if ice[x][y] <= 0:
            ice[x][y] = 0
            l_tmp -= 1
        else:
            s, e = x, y
    ans += 1

    k = dfs(s, e)
    if l_tmp == 0:
        print(0)
        break
    if k != l_tmp:
        print(ans)
        break
