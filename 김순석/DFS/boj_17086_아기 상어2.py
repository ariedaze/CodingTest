# pypy로 제출함
# 경쟁적 전염문제로 풀어야할듯
import sys
from collections import deque

sys.stdin = open('input/boj_17086_아기 상어2.txt', 'r')
In = sys.stdin.readline

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

arr = []

N, M = map(int, In().split())
for _ in range(N):
    arr.append(list(map(int, In().split())))


def bfs(x, y):
    memo = [[0] * M for _ in range(N)]
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(8):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or tx >= N or ty < 0 or ty >= M: continue
            if arr[tx][ty] == 0 and memo[tx][ty] == 0:

                memo[tx][ty] = memo[x][y] + 1
                q.append((tx, ty))
            elif arr[tx][ty] == 1:
                return memo[x][y] + 1

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            k = bfs(i, j)
            if ans < k:
                ans = k
print(ans)