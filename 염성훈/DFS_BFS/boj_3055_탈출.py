import sys
from collections import deque
sys.stdin = open("input.txt","r")

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or tx == n or ty < 0 or ty == m:
                continue
            if visited[tx][ty] == 0 and visited[x][y] == -1 and arr[tx][ty] != 'X' and arr[tx][ty] != 'D':
                visited[tx][ty] = -1
                q.append([tx,ty])
            elif visited[tx][ty] == 0 and visited[x][y] >= 1 and arr[tx][ty] != 'X':
                visited[tx][ty] = visited[x][y] + 1
                q.append([tx, ty])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int,input().split()) # n: 세로 m:가로

arr = [list(map(str,input())) for _ in range(n)]
visited = [[0] * m for  _ in range(n)]

q = deque()
ex, ey = 0, 0
# 물을 먼저 넣어줘야한다. 그래야 q에서 먼저 빠져나와서 로직을 돌기 때문에 먼저 vistied처리가되서
# 고슴도치와 물이 같은시간에 한칸을 들어가야할때 물이 먼저 들어가 고슴도치가 안들어가게 할 수 있음.
for x in range(n):
    for y in range(m):
        if arr[x][y] == '*':
            q.append([x,y])
            visited[x][y] = -1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            q.append([i,j])
            visited[i][j] = 1
        elif arr[i][j] == 'D':
            ex,ey = i, j

bfs()

if visited[ex][ey]:
    print(visited[ex][ey] - 1)
else:
    print("KAKTUS")
