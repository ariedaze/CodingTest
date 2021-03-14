# 컴퓨터수 N, 간선 수 M
N = int(input())
M = int(input())
visit = [0] * (N + 1)
count = 0
G = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    v, e = map(int, input().split())
    G[v][e] = G[e][v] = 1


def dfs(v):
    global count
    visit[v] = 1
    for w in range(1, N + 1):
        if visit[w] == 0 and G[v][w] == 1:
            count += 1
            dfs(w)


dfs(1)
print(count)

