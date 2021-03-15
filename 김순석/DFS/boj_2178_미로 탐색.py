import sys
from collections import deque

sys.stdin = open('input/boj_2178_미로 탐색.txt', 'r')
In = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, In().split())
arr = []
q = deque()
for _ in range(N):
    arr.append(list(map(int, In().rstrip())))


def bfs(x, y):
    q.append((x, y))
    arr[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or tx >= N or ty < 0 or ty >= M or arr[tx][ty] == 0:
                continue
            if tx == N - 1 and ty == M - 1:
                return arr[x][y] + 1
            if arr[tx][ty] == 1:
                arr[tx][ty] = arr[x][y] + 1

                q.append((tx, ty))

ans = bfs(0, 0)
print(ans)
