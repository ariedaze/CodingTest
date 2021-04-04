from collections import deque

N = int(input())
e = int(input())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(e):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

Q = deque([1])
visited[1] = 1
cnt = 0

while Q:
    v = Q.popleft()
    for w in graph[v]:
        if not visited[w]:
            Q.append(w)
            visited[w] = 1
            cnt += 1


print(cnt)
