from collections import deque


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

tree = [[] for _ in range(n+1)]
visited = [0] * (n+1)
answer = -1

for _ in range(m):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

Q = deque([(p1, 0)])
visited[p1] = 1

while Q:
    v, cnt = Q.popleft()

    if v == p2:
        answer = cnt
        break

    for w in tree[v]:
        if not visited[w]:
            Q.append((w, cnt+1))
            visited[w] = 1


print(answer)
