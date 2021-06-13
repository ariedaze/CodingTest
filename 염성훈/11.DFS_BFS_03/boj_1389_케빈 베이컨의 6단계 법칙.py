import sys
sys.stdin = open("input.txt", "r")
from collections import deque

def bfs(s,n):
    distance = [0] * (n + 1)
    q = deque()
    q.append(s)
    while q:
        x = q.popleft()
        for w in gragh[x]:
            if not visited[w]:
                distance[w] = distance[x] + 1
                visited[w] = 1
                q.append(w)

    return sum(distance)



n, m = map(int,input().split()) #n: 유저의 수, m: 친구 관계의 수
gragh = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int,input().split())
    gragh[s].append(e)
    gragh[e].append(s)

result = []
for i in range(1,n +1):
    visited = [0] * (n + 1)
    result.append(bfs(i,n))

for idx, value in enumerate(result):
    if value == min(result):
        print(idx + 1)
        break


