import sys
sys.stdin = open("input.txt")

def dfs(s):
    global ans
    visited[s] = 1
    for w in graph[s]:
        if not visited[w]:
            ans += 1
            dfs(w)

V = int(input())
E = int(input())

graph = [[] for _ in range(V + 1)]
visited = [0] * (V + 1)

ans = 0

for _ in range(E):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

dfs(1)

print(ans)
