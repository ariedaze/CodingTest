from collections import deque

N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]


def dfs(v):
    print(v, end=' ')
    visited[v] = 1

    for w in graph[v]:
        if graph[v][w] and not visited[w]:
            dfs(w)


def bfs(v):
    Q = deque([v])
    visited[v] = 1
    while Q:
        q = Q.popleft()
        print(q, end=' ')
        for w in graph[q]:
            if graph[q][w] and not visited[w]:
                Q.append(w)
                visited[w] = 1


for _ in range(M):
    v, w = map(int, input().split())
    graph[v][w] = w
    graph[w][v] = v


visited = [0]*(N+1)
dfs(V)
print()
visited = [0]*(N+1)
bfs(V)

