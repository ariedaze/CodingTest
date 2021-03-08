import sys
from collections import deque

sys.stdin = open("input.txt","r")

def dfs(s):
    visited[s] = 1
    for w in graph[s]:
        if not visited[w]:
            visited[w] = 1
            print(w, end=" ")
            dfs(w)

def bfs(s):
    Q = deque([])
    Q.append(s)
    visited[s] = 1

    while Q:
        v = Q.popleft()
        print(v, end=" ")
        for w in graph[v]:
            if not visited[w]:
                visited[w] = 1
                Q.append(w)



N, M, V = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
result = []

for i in range(M):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(N+1): #작은 수대로 노드를 출력해야하므로 2차원 배열안의 값을 한번 더 오름차순으로 정렬해준다.
    graph[i].sort()

print(V, end=" ")
dfs(V)
visited = [0] * (N+1)
print()
bfs(V)

