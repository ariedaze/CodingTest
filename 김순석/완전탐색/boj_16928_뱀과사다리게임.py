import sys
from collections import deque
ln = sys.stdin.readline

N, M = map(int, ln().split())
graph = [i for i in range(101)]
visit = [-1] * 101

for _ in range(N):
    x, y = map(int, ln().split())
    graph[x] = y
for _ in range(M):
    u, v = map(int, ln().split())
    graph[u] = v


def bfs(x):
    q = deque()
    q.append(x)
    visit[x] = 0
    while q:
        x = q.popleft()
        for i in range(1, 7):
            tx = x + i
            if tx > 100:
                continue
            tx = graph[tx]
            if visit[tx] == -1 or visit[tx] > visit[x] + 1:
                visit[tx] = visit[x] + 1
                q.append(tx)

bfs(1)
print(visit[-1])
