import sys
from collections import deque
ln = sys.stdin.readline

N, M = map(int, ln().split())
arr = [[] for _ in range(N + 1)]
arr[0] = [0]

def bfs(v):
    q = deque()
    q.append((arr[v], 1))
    graph[v][v] = 0
    while q:
        lst, depth = q.popleft()
        for w in lst:
            if v != w and not visit[v][w]:
                visit[v][w] = 1
                graph[v][w] = depth
                q.append((arr[w], depth + 1))


for i in range(M):
    s, e = map(int, ln().split())
    arr[s].append(e)
    arr[e].append(s)


graph = [[0] * (N + 1) for _ in range(N + 1)]
visit = [[0] * (N + 1) for _ in range(N + 1)]

min_val = 0xfffff
ans = 0
for i in range(1, N + 1):
    bfs(i)
    if min_val > sum(graph[i]):
        min_val = sum(graph[i])
        ans = i
print(ans)