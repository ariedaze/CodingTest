import sys
ln = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
r, c = map(int, ln().split())
s, e, d = map(int, ln().split())

arr = [list(map(int, ln().split())) for _ in range(r)]
ans = 0


def dfs(x, y, d):
    global ans

    if arr[x][y] == 0:
        arr[x][y] = -1
        ans += 1

    for i in range(4):
        # 0 -> 3, 1 -> 0, 2 -> 1, 3 -> 2
        td = (d + 3) % 4
        tx, ty = x + dx[td], y + dy[td]

        # 2.a 왼쪽방향 청소
        if arr[tx][ty] == 0:
            dfs(tx, ty, td)
            return
        # 2.b 회전 시킨다
        d = td

    # 뒤로이동
    td = (d + 2) % 4
    tx, ty = x + dx[td], y + dy[td]

    # 뒤가벽이면
    if arr[tx][ty] == 1:
        return
    # 방향은유지
    dfs(tx, ty, d)

dfs(s, e, d)
print(ans)