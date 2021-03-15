import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]
visit = [0] * (N + 1)
for i in range(M):
    s, e = map(int, input().split())
    arr[s][e] = arr[e][s] = 1


def dfs(v):
    visit[v] = 1
    print(v, end=' ')
    for w in range(1, N + 1):
        if visit[w] == 0 and arr[v][w] == 1:
            dfs(w)


dfs(V)
print()


q = deque()
visit = [0] * (N + 1)

def bfs(v):
    q.append(v)
    visit[v] = 1

    while q:
        v = q.popleft()
        print(v, end=' ')
        for w in range(1, N + 1):
            if visit[w] == 0 and arr[v][w] == 1:
                q.append(w)
                visit[w] = 1

bfs(V)
