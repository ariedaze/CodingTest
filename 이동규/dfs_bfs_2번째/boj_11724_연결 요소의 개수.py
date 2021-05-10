import sys
sys.stdin = open('input/boj_11724_연결 요소의 개수.txt', 'r')

from collections import deque

def bfs(start, maps, visited):
    queue = deque()
    queue.append(start)
    while queue:
        y = queue.popleft()
        visited.add(y)
        for x in range(1, len(maps[y])):
            if maps[y][x] == 1 and x not in visited:
                visited.add(x)
                queue.append(x)
    return 1

n, m = map(int, sys.stdin.readline().split())
maps = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    y, x = map(int, sys.stdin.readline().split())
    maps[y][x] = 1
    maps[x][y] = 1

visited = set()
answer = 0
for y in range(1, len(maps)):
    if y not in visited:
        visited.add(y)
        answer += bfs(y, maps, visited)
print(answer)