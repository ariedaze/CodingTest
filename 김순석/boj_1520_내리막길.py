import sys
sys.setrecursionlimit(10**6)
ln = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

M, N = map(int, ln().split())
arr = []
dp = [[-1] * N for _ in range(M)]

for _ in range(M):
    arr.append(list(map(int, ln().split())))


def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]

        if tx < 0 or tx >= M or ty < 0 or ty >= N:
            continue

        if arr[tx][ty] < arr[x][y]:
            dp[x][y] += dfs(tx, ty)

    return dp[x][y]

# dfs(0, 0)
print(dfs(0, 0))
# print(dp[-1][-1])
