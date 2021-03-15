import sys
sys.stdin = open('input/boj_1743_음식물 피하기.txt', 'r')
In = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M, K = map(int, In().split())
arr = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, In().split())
    arr[r-1][c-1] = 1


def dfs(x, y):

    cnt = 1
    s = [[x, y]]
    arr[x][y] = 0

    while s:
        x, y = s.pop()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or tx >= N or ty < 0 or ty >= M or arr[tx][ty] == 0:
                continue
            if arr[tx][ty] == 1:
                cnt += 1
                arr[tx][ty] = 0
                s.append((tx, ty))
    return cnt

ans = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            x = dfs(i, j)
            if ans < x:
                ans = x
print(ans)