import sys
sys.stdin = open('input/boj_1303_전투.txt', 'r')
sys.setrecursionlimit(10 ** 6)
In = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, In().split())
arr = []
visit = [[0] * N for _ in range(M)]
for i in range(M):
    arr.append(In().rstrip())


def dfs(x, y):
    s = [[x, y]]
    visit[x][y] = 1
    area = 1

    while s:
        x, y = s.pop()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if tx <= -1 or tx >= M or ty <= -1 or ty >= N:
                continue

            if visit[tx][ty] == 0 and arr[x][y] == arr[tx][ty]:
                visit[tx][ty] = 1
                area += 1
                s.append([tx, ty])

    return area ** 2


ans1 = ans2 = 0
for i in range(M):
    for j in range(N):
        if visit[i][j] == 0 and arr[i][j] == 'W':
            ans1 += dfs(i, j)
        elif visit[i][j] == 0 and arr[i][j] == 'B':
            ans2 += dfs(i, j)

print(ans1, ans2)