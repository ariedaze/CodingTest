import sys
sys.stdin = open("input.txt","r")

from collections import deque


def bfs(x,y):
    Q = deque([])
    Q.append([x,y])
    visited[x][y] = 1

    while Q:
        cx, cy = Q.popleft()
        for i in range(4):
            tx, ty = cx+dx[i], cy+dy[i]
            if tx < 0 or tx == N or ty < 0 or ty == M:
                continue
            if arr[tx][ty] and not visited[tx][ty]:
                visited[tx][ty] = visited[cx][cy] + 1
                Q.append([tx,ty])



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int,input().split()) #N이 세로, M이 가로

arr = [list(map(int,input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

bfs(0,0)

print(visited[N-1][M-1])

