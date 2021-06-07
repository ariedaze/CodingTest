import sys
sys.stdin = open("input.txt","r")
from collections import deque


def bfs(node):
    q = deque()
    q.append(node)
    check[node] = 0
    while q:
        node = q.popleft()
        for i in range(1, 7):
            n = node + i
            if n > 100:
                continue
            # 다음으로 넘어갈 부분의 인덱스 값
            t = graph[n]
            # 안들린 노드이면 들리고 다시 q에 넣는다.
            if check[t] == -1:
                q.append(t)
                check[t] = check[node] + 1


N, M = map(int, input().split())
graph = [i for i in range(101)]
check = [-1] * 101
for _ in range(N):
    u, v = map(int, input().split())
    graph[u] = v
for _ in range(M):
    u, v = map(int, input().split())
    graph[u] = v

bfs(1)
print(check[100])