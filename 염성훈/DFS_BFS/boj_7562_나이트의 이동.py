import sys
from collections import deque
sys.stdin = open("input.txt","r")

def bfs(sx, sy, ex, ey):
    q = deque()
    q.append([sx,sy])
    visited[sx][sy] = 0
    while q:
        a, b = q.popleft()
        if a == ex and b == ey:
            return visited[a][b]
        for i in range(8):
            tx, ty = a + dx[i], b + dy[i]
            if tx < 0 or tx >= n or ty < 0 or ty >= n:
                continue
            if not visited[tx][ty]:
                visited[tx][ty] = visited[a][b] + 1
                q.append([tx,ty])


dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input())

for _ in range(T):
    n = int(input())
    sx, sy = map(int,input().split())
    ex, ey = map(int,input().split())
    visited = [[0] * n for _ in range(n)]
    ans = bfs(sx, sy, ex, ey)
    print(ans)