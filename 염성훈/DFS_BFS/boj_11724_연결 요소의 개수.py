import sys
sys.stdin = open("input.txt","r")
sys.setrecursionlimit(10000)

def dfs(s):
    visited[s] = True
    for w in graph[s]:
        if not visited[w]:
            visited[w] = True
            dfs(w)

N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
ans = 0

for _ in range(M):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N+ 1):
    if not visited[i]:
        ans += 1
        dfs(i)

print(ans)