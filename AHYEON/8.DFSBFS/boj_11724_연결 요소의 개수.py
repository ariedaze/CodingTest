from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
answer = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, N+1):
    if visited[i]: continue
    Q = deque([i])
    visited[i] = 1
    answer += 1
    while Q:
        x = Q.popleft()
        for y in graph[x]:
            if visited[y]: continue
            Q.append(y)
            visited[y] = 1

print(answer)