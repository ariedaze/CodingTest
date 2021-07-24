from collections import deque

def bfs(visited, graph):
    q = deque()
    q.append(1)
    visited[1] = 1

    while q:
        node = q.popleft()
        for w in graph[node]:
            if not visited[w]:
                visited[w] += visited[node] + 1
                q.append(w)


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for line in edge:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])

    visited = [0] * (n + 1)
    bfs(visited, graph)

    for i in visited:
        if i == max(visited):
            answer += 1

    return answer

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, vertex)