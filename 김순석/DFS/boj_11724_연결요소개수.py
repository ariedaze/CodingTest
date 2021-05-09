import sys
ln = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(v):
    visit[v] = 1
    for i in G[v]:
        if not visit[i]:
            dfs(i)



N, M = map(int, ln().split())

G = [[0] for _ in range(N + 1)]
visit = [0] * (N + 1)
for _ in range(M):
    s, e = map(int, ln().split())
    G[s].append(e)
    G[e].append(s)

# print(G)

cnt = 0
for i in range(1, N + 1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)

