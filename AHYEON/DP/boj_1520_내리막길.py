import sys
sys.setrecursionlimit(10 ** 8)
# sys.stdin = open('input/boj_1520_내리막길.txt', 'r')
input = sys.stdin.readline


def dfs(x, y, W, result):
    if result[y][x] != -1:
        return result[y][x]
    tmp = 0
    for mode in range(4):
        nx, ny = x + dx[mode], y + dy[mode]
        if 0 <= nx < M and 0 <= ny < N and W[y][x] > W[ny][nx]:
            tmp += dfs(nx, ny, W, result)
    result[y][x] = tmp

    return result[y][x]


N, M = map(int, input().split())
W = [list(map(int, input().split())) for _ in range(N)]
result = [[-1]*M for _ in range(N)]
result[N - 1][M - 1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(dfs(0, 0, W, result))